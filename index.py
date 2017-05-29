from flask import Flask, render_template, request, redirect, url_for, send_from_directory, g
from bs4 import BeautifulSoup
import os
import requests
import pandas as pd
import numpy

app = Flask(__name__)


dirpath = os.path.join(app.root_path,'download')

@app.route('/')
def index():
    
    filename = request.args.get('filename')

    return render_template('index.html', filename=filename)

@app.route('/crawler', methods=['POST'])
def crawler():

    df = pd.DataFrame()

    #df = pd.DataFrame([{'term':0,'date':0,'1st':0,'2nd':0,'3rd':0,'4th':0,'5th':0}])

    for i in range(106000001,106000025):

        payload = {
        "__EVENTTARGET":"",
        "__EVENTARGUMENT":"",
        "__LASTFOCUS":"",
        "__VIEWSTATE":"/wEPDwULLTExOTIxMTcwNTkPZBYCAgEPZBYCAgMPZBYMAgEPEGRkFgECBGQCAw8QDxYCHgdDaGVja2VkZ2RkZGQCCQ8QZGQWAQIDZAILDxBkZBYBAgNkAg8PDxYCHgRUZXh0ZWRkAhEPPCsACQEADxYEHghEYXRhS2V5cxYAHgtfIUl0ZW1Db3VudAIBZBYCZg9kFi4CAQ8PFgIfAQUJMTAzMDAwMDAxZGQCAw8PFgIfAQUJMTAzLzAxLzAxZGQCBQ8PFgIfAQUCMjZkZAIHDw8WAh8BBQIxM2RkAgkPDxYCHwEFAjA1ZGQCCw8PFgIfAQUCMzRkZAINDw8WAh8BBQIyNGRkAg8PDxYCHwEFCTEwMy8wNC8wMWRkAhEPDxYCHwEFAjA1ZGQCEw8PFgIfAQUCMTNkZAIVDw8WAh8BBQIyNGRkAhcPDxYCHwEFAjI2ZGQCGQ8PFgIfAQUCMzRkZAIbDw8WAh8BBQo0Nyw4MTcsMTAwZGQCHQ8PFgIfAQUKMjAsNTE4LDUwMGRkAh8PDxYCHwEFATFkZAIhDw8WAh8BBQMyNjRkZAIjDw8WAh8BBQU4LDQ3N2RkAiUPDxYCHwEFBjkzLDkwOGRkAicPDxYCHwEFCTgsMDAwLDAwMGRkAikPDxYCHwEFBjIwLDAwMGRkAisPDxYCHwEFAzMwMGRkAi0PDxYCHwEFAjUwZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgMFGkQ1MzlDb250cm9sX2hpc3RvcnkxJHJhZE5PBRpENTM5Q29udHJvbF9oaXN0b3J5MSRyYWRZTQUaRDUzOUNvbnRyb2xfaGlzdG9yeTEkcmFkWU17ZHQFBn6C4YXQMxwTrjO+iRVdq2HFussNeP4ud6CR+g==",
        "__VIEWSTATEGENERATOR":"09BD3138",
        "__EVENTVALIDATION":"/wEWIALEz6rLBALMm6OFDQLc9InrAQLD9InrAQLC9InrAQLD9MXoAQLH9InrAQLG9InrAQLF9InrAQLA9InrAQLB9InrAQLD9MnoAQLX4LOKDALSmZOFDALR4M+ABwKZq6PUDwL2kcGiAgLT/ueJCAKo54WUDgLAydWcDwLBydWcDwLCydWcDwLDydWcDwLEydWcDwLFydWcDwLGydWcDwLXydWcDwLYydWcDwLAyZWfDwLAyZmfDwLAyZ2fDwLuno2BDW0KS57wKrk1X7mVCyXQD+dd9+qfzbz9APJfDg6IUNxl",
        "D539Control_history1$DropDownList1":"5",
        "D539Control_history1$chk":"radNO",
        "D539Control_history1$txtNO":str(i),
        "D539Control_history1$btnSubmit":"查詢"
        }
        
        payload1 = {
        "__EVENTTARGET":"",
        "__EVENTARGUMENT":"",
        "__LASTFOCUS":"",
        "__VIEWSTATE":"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",
        "__VIEWSTATEGENERATOR":"09BD3138",
        "__EVENTVALIDATION":"/wEWIAL2q+H1CwLMm6OFDQLc9InrAQLD9InrAQLC9InrAQLD9MXoAQLH9InrAQLG9InrAQLF9InrAQLA9InrAQLB9InrAQLD9MnoAQLX4LOKDALSmZOFDALR4M+ABwKZq6PUDwL2kcGiAgLT/ueJCAKo54WUDgLAydWcDwLBydWcDwLCydWcDwLDydWcDwLEydWcDwLFydWcDwLGydWcDwLXydWcDwLYydWcDwLAyZWfDwLAyZmfDwLAyZ2fDwLuno2BDVwmHltbPlQ03n/tID1g5dRtzyXY/5i3rfZG5TUxR9yx",
        "D539Control_history1$DropDownList1":"5",
        "D539Control_history1$chk":"radNO",
        "D539Control_history1$txtNO":str(i),
        "D539Control_history1$btnSubmit":"查詢"
        }

        res_post = requests.post("http://www.taiwanlottery.com.tw/Lotto/Dailycash/history.aspx",data = payload1)
        #print (res_post.text)

        soup = BeautifulSoup(res_post.text,'html.parser')
        table = soup.find('td')
        #print (table.text)
        
        drawterm = soup.find('span', attrs={'id' : 'D539Control_history1_dlQuery_D539_DrawTerm_0'})    
        #print (drawterm.text)
        n1t = drawterm.text
        
        ddate = soup.find('span', attrs={'id' : 'D539Control_history1_dlQuery_D539_DDate_0'})    
        #print (ddate.text)
        n2t = ddate.text
        
        n3 = soup.find('span', attrs={'id' : 'D539Control_history1_dlQuery_No1_0'})
        n3t = n3.text
        
        n4 = soup.find('span', attrs={'id' : 'D539Control_history1_dlQuery_No2_0'})
        n4t = n4.text
        
        n5 = soup.find('span', attrs={'id' : 'D539Control_history1_dlQuery_No3_0'})
        n5t = n5.text
        
        n6 = soup.find('span', attrs={'id' : 'D539Control_history1_dlQuery_No4_0'})
        n6t = n6.text
        
        n7 = soup.find('span', attrs={'id' : 'D539Control_history1_dlQuery_No5_0'})
        n7t = n7.text
        
        print (n1t,n2t,n3t,n4t,n5t,n6t,n7t) #列出期號，可得知程式執行進度
        #print (n2t)
        #print (n3t)
        #print (n4t)
        #print (n5t)
        #print (n6t)
        #print (n7t)
        
        #將開獎號碼依照開獎期數存入 DataFrame
        df = df.append(pd.DataFrame([{'term':int(n1t),'date':n2t,'1st':int(n3t),'2nd':int(n4t),'3rd':int(n5t),'4th':int(n6t),'5th':int(n7t)}]))

        out = df.to_json(orient='records')

        with open('./download/539.txt', 'w') as f:
            f.write(out)
    
    return render_template('index.html', filename=out)
    #return send_from_directory(dirpath,filename,as_attachment=True)


@app.route('/download', methods=['POST'])
def download():

    filename = '539.txt'

    return send_from_directory(dirpath,filename,as_attachment=True)


if __name__ == '__main__':
    app.run(host='0.0.0.0',port=9000,debug=True)
