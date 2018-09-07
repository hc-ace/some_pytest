# -*- coding:UTF-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import requests
import os
import time
import re
from PIL import Image
from io import BytesIO
if __name__ == '__main__':
    for num in range(1850,1900):    #批量处理
        url = 'http://www.vividict.com/WordInfo.aspx?id='+str(num)
        headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
        }                           #代理
        req = requests.get(url = url,headers = headers)
        req.encoding = 'utf-8'
        html = req.text
        bf = BeautifulSoup(html, 'lxml')    #页面内容
        targets_url = bf.find_all(hspace='2')   #找关键字
        pathDir = 'f:\\pytest\\p1\\'            #用来比较重复文件
        for each in targets_url:
            list_url=each.get('src')
#            print(list_url)
            if(list_url[0:4]!='http'):
                list_url='http://www.vividict.com'+list_url
            img_info = list_url.split('/')
#            print(list_url)
            if(img_info[-1][-7:]=='(1).gif'):
                if(img_info[-1][3:6]=='jia'):
                    filename = 'jia'+str(num)
                if(img_info[-1][3:6]=='jin'):
                    filename = 'jin'+str(num)
                if(img_info[-1][3:6]=='kai'):
                    filename = 'kai'+str(num)
                if(img_info[-1][3:5]=='li'):
                    filename = 'li'+str(num)
                if(img_info[-1][3:8]=='zhuan'):
                    filename = 'zhuan'+str(num)
                if(img_info[-1][3:6]=='cao'):
                    filename = 'cao'+str(num)
                if(img_info[-1][3:5]=='zh'):
                    filename = 'zh'+str(num)
                for n in range(1,3):
                    if(os.path.exists(pathDir + filename + '.gif' )):
                        filename = filename + '(1)'
                    else:
                        break
                print('下载：' + filename)  
                response = requests.get(list_url)
                image = Image.open(BytesIO(response.content))
                image.save('f:\\pytest\\p1\\%s.gif' %filename)
                time.sleep(1)
                continue
            if(img_info[-1][-6:]!='00.gif'):
                continue
            if(img_info[-1][2:5]=='jia'):
                filename = 'jia'+str(num)
            if(img_info[-1][2:5]=='jin'):
                filename = 'jin'+str(num)
            if(img_info[-1][2:5]=='kai'):
                filename = 'kai'+str(num)
            if(img_info[-1][2:4]=='li'):
                filename = 'li'+str(num)
            if(img_info[-1][2:7]=='zhuan'):
                filename = 'zhuan'+str(num)
            if(img_info[-1][2:5]=='cao'):
                filename = 'cao'+str(num)
            if(img_info[-1][2:4]=='zh'):
                filename = 'zh'+str(num)
            for n in range(1,3):
                if( os.path.exists(pathDir + filename + '.gif' )):
                    filename = filename + '(1)'
                else:
                    break
            print('下载：' + filename) 
            response = requests.get(list_url)
            image = Image.open(BytesIO(response.content))
            image.save('f:\\pytest\\p1\\%s.gif' %filename)
            time.sleep(1)
        print('下载完成！')
        time.sleep(1)