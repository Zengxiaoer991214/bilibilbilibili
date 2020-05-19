import re
import requests
from lxml import etree
class rank:
    def __init__(self):
        url = 'https://www.bilibili.com/ranking/all/0/0/3'
        headers = {
            'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 Edg/81.0.416.72',
            'X-Requested-With':'XMLHttpRequest'
        }
        request = requests.get(url, headers = headers)
        self.text = request.text
        #print(request.text)
    def get_url(self):
        url_dic = [ ]
        html = etree.HTML(self.text)
        urls = html.xpath('//li[@class="rank-item"]/div[2]/div[@class="info"]/a/@href')
        names = html.xpath('//li[@class="rank-item"]/div[2]/div[@class="info"]/a/text()')
        for url, name in zip(urls, names):
            url_dic.append({"url":url, "name":name})
 
        return url_dic
        
r = rank()
r.get_url()