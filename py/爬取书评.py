#爬虫网络资源，抓取与解析
#抓取 urllib.request scrapy框架
#解析 BeautifulSoup库 re模块 
import requests
import re
from bs4 import BeautifulSoup
'''
#爬取书评
sum=0
r = requests.get("https://book.douban.com/subject/30145197/?icn=index-editionrecommend")
a=r.status_code
soup = BeautifulSoup(r.text,"lxml")
pattern = soup.find_all('p','comment-content')
for i in pattern:
    print(i)
#数据解析re正则表达式，常用(.*?)
pattern_s = re.compile('<span class="user-stars allstar(.*?) rating"')
p=re.findall(pattern_s,r.text)
for i in p:
    sum += int(i)
print(sum)
'''
def retrieve_dji_list():
    r=requests.get('http://money.cnn.com/data/dow30/')
    pattern= re.compile()
