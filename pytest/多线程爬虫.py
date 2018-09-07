# -*- coding: utf-8 -*-
"""
Created on Fri Jul 27 11:07:30 2018

@author: am
"""

#!/usr/bin/env python2
# -*- coding=utf-8 -*-

from threading import Thread
from queue import Queue
import time
from lxml import etree
import requests


class DouBanSpider(Thread):
    def __init__(self, url, q):
        # 重写写父类的__init__方法
        super(DouBanSpider, self).__init__()
        self.url = url
        self.q = q
        self.headers = {
                'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'
        }  
    def run(self):
        self.parse_page()

    def send_request(self,url):
        '''
        用来发送请求的方法
        :return: 返回网页源码
        '''
        # 请求出错时，重复请求３次,
        i = 0
        while i <= 3:
            try:
                print(u"[INFO]请求url:"+url)
                html = requests.get(url=url,headers=self.headers).content
            except Exception as e:
                print(u'[INFO] %s%s'% (e,url))
                i += 1
            else:
                return html

    def parse_page(self):
        '''
        解析网站源码，并采用ｘｐａｔｈ提取　电影名称和平分放到队列中
        :return:
        '''
        response = self.send_request(self.url)
        html = etree.HTML(response)
        #　获取到一页的电影数据
        node_list = html.xpath("//div[@class='info']")
        with open('f:\\pytesttxt\\aa.txt', 'w', encoding='utf-8') as f:
            f.writelines(str(node_list))
        for move in node_list:
            # 电影名称
            title = move.xpath('.//a/span/text()')[0]
            # 评分
            score = move.xpath('.//div[@class="bd"]//span[@class="rating_num"]/text()')[0]

            # 将每一部电影的名称跟评分加入到队列
            self.q.put(score + "\t" + title)


def main():
    # 创建一个队列用来保存进程获取到的数据
    q = Queue()
    base_url = 'https://movie.douban.com/top250?start='
    # 构造所有ｕｒｌ
    url_list = [base_url+str(num) for num in range(546,4016)]

    # 保存线程
    Thread_list = []
    # 创建并启动线程
    for url in url_list:
        p = DouBanSpider(url,q)
        p.start()
        Thread_list.append(p)

    # 让主线程等待子线程执行完成
    for i in Thread_list:
        i.join()

    while not q.empty():
        print(q.get())

if __name__=="__main__":

    start = time.time()
    main()
    print('[info]耗时：%s'%(time.time()-start))


