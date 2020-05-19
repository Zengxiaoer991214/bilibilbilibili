import time
import re
import requests
from lxml import etree
from wordcloud import WordCloud
import PIL .Image as image
import numpy as np
import jieba
import get_urls
import random
import get_oids
import os
import shutil
import string_func as sf
import images
import save_danmu as s_d
class B:
    def __init__(self,url):
        self.headers={
        'Host': 'api.bilibili.com',
        'Connection': 'keep-alive',
        'Cache-Control': 'max-age=0',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36',
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cookie': 'finger=edc6ecda; LIVE_BUVID=AUTO1415378023816310; stardustvideo=1; CURRENT_FNVAL=8; buvid3=0D8F3D74-987D-442D-99CF-42BC9A967709149017infoc; rpdid=olwimklsiidoskmqwipww; fts=1537803390'
        }
        oid = get_oids.get_oid(url)
        self.url='https://api.bilibili.com/x/v1/dm/list.so?oid='+str(oid)
        self.barrage_reault=self.get_page()
    def get_page(self):
        try:
            response=requests.get(self.url,headers=self.headers)
        except Exception as e:
            print('获取xml内容失败,%s' % e)
            return False
        else:
            if response.status_code == 200:
                self.html = response
                return True
            else:
                return False
    def param_page(self):
        xml = etree.fromstring(self.html.content)    
        # xpath解析，获取当前所有的d标签下的所有文本内容
        results = xml.xpath('//d//text()')
        # /html/body/svg/symbol[10]/path
        self.results = results
        return results

    def simple_danmu(self):
        dicc = {" ":0}
        sf.string_io(dicc, self.results)
        dic = {}  
        sf.string_io2(dic, dicc)
        dic = sorted(dic.items(), key=lambda item:item[1], reverse=True)
        dic_sort = {}
        for i in dic:
            dic_sort.setdefault(i[0],i[1])
            #print(i[0],i[1])
        s_d.saveFile(dic_sort)
        s_d.saveFile2(self.results)
        text = ""
        index = 0
        dic_image = {}
        for i in dic_sort:
            text += i
            dic_image[i] = dic_sort[i]
            index += 1
            if index == 9:
                break
        self.text =text
        sum1 = sum(list(dic_sort.values())) 
        sum2 = sum(list(dic_image.values())) 
        dic_image["其他弹幕"] = sum1 - sum2

        im = images.image_save(dic_image)
        im.zhifang()
        im.func()
        
    def trans_CN(self):
        zhmodel = re.compile(u'[\u4e00-\u9fa5]')    #检查中文
        match = zhmodel.search(self.text)
        if match:
            word_list = jieba.cut(self.text)
            result = " ".join(word_list)
            return result
        else:
            return self.text+"弹幕无法解析"
   
    def word_cloud(self,img_name):
        self.img_name = img_name
        mask = np.array(image.open("D:\\1.PNG"))
        wordcloud = WordCloud(
            mask = mask,
            font_path = "simsun.ttc"
        ).generate(self.trans_CN())
        img = img_name+".png"
        wordcloud.to_file(img)
        wordcloud.to_image()
        #image_produce.show()
        os.makedirs(img_name)
        shutil.move(img,img_name)
        shutil.move("zhifangtu.png",self.img_name)
        shutil.move("sanxingtu.png",self.img_name)
        shutil.move("danmu.json",self.img_name)
        shutil.move("danmu2.json",self.img_name)
def run(url):
    b = B(url['url'])
    b.get_page()
    b.param_page()
    b.simple_danmu()
    b.word_cloud(url['name'])
url = {"url":"https://www.bilibili.com/video/BV1WE411d7Dv","name":"test"}
run(url)

# if __name__ == "__main__":
#     r = get_urls.rank()
#     index = 0
#     for i in r.get_url():
#         index += 1
#         print(index, "is starting")
#         if  index <= 2:
#             run(i)

# def simple_danmu(self):
#         dic = {}
#         dic_key = []
#         for i in self.results:
#             #print(dic)
#             #print("")
#             #print(i)
#             if sf.string_io(dic_key,i):
#                 #print(" yes", sf.string_io(dic_key,i))
#                 dic[sf.string_io(dic_key,i)] += 1
#             else:
#                 #print("第一次添加————")
#                 dic[i] = 1
#                 dic_key.append(i)
#         dic = sorted(dic.items(), key=lambda item:item[1], reverse=True)
#         dic_sort = {}
#         for i in dic:
#             dic_sort.setdefault(i[0],i[1])
#             #print(i[0],i[1])
#         text = ""
#         index = 0
#         dic_image = {}
#         for i in dic_sort:
#             text += i
#             dic_image[i] = dic_sort[i]
#             index += 1
#             if index > 10:
#                 break
#         self.text =text
#         #print("弹幕总和"+text)
#         im = images.image_save(dic_image)
#         im.zhifang()
#         im.func()
#         shutil.move("zhifangtu.png",self.img_name)
#         shutil.move("sanxingtu.png",self.img_name)