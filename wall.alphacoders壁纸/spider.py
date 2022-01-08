# -*- coding: utf-8 -*-
# @Time: 2021/12/31 16:36
# @File : spider.py
import os
import re
import threading
from queue import Queue
import requests
from lxml import etree
from choose import choose

class GetImgUrl(threading.Thread):
    def __init__(self,PageQueue,ImgQueue):
        super(GetImgUrl, self).__init__()
        self.PageQueue=PageQueue
        self.ImgQueue=ImgQueue
        self.headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    def run(self):
        while True:
            # if self.ImgQueue.empty():
            #     break
            #从队列中获取一个数据
            page_url=self.PageQueue.get()
            print(page_url)
            self.parse(page_url)
    def parse(self,page_url):
        response=requests.get(page_url,headers=self.headers)
        #获取重定向后的链接
        url=response.url
        html=requests.get(url,headers=self.headers).text
        html=etree.HTML(html)
        img_list=html.xpath('//div[@class="boxgrid"]')
        for img in img_list:
            title=img.xpath("./a/@href")[0]
            '''
                 这里的xpath是定位到class=boxgrid 然后定位到img
                 浏览器能看到数据，解析却不行，直接输出etree.HTML()后的源码发现
                 这个网站有很多"语法错误"，许多标签没有</*>表示结束，例如<source> 导致解析的路径和Chrome浏览器获取的路径不一样
                 离谱呀
            '''
            src = img.xpath("./a/picture/source/source/source/img/@src")[0]
            # 匹配不是数字的其他字符
            drop = re.compile("[^0-9]")
            # 将中匹配到的字符替换成空字符
            title = drop.sub('', title)
            #获取高清图片链接 这里直接把 thumbbig- 替换为空就得到链接
            src=src.replace('thumbbig-','')
            #获取图片格式
            suffix = os.path.splitext(src)[1]
            #最后的文件名
            filename=str(title)+suffix
            #存到队列
            self.ImgQueue.put((filename,src))
class DownloadImg(threading.Thread):
    def __init__(self,ImgQueue,name):
        super(DownloadImg, self).__init__()
        self.ImgQueue = ImgQueue
        self.name=name
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
    def run(self):
        while True:
            #获取一个数据
            filename,img=self.ImgQueue.get()
            self.Dwonload(filename,img)
    def Dwonload(self,filename,img):
        try:
            resp = requests.get(img, headers=self.headers)
            if resp.status_code!=200:
                print("恭喜你请求失败了！！！"%resp.status_code)
            #设置保存路径 +选择的壁纸类别+文件名为图片id
            path='E:/Wallpaper/'+self.name+'/'
            #如果目录不存在则创建目录
            if not os.path.exists(path):
                os.makedirs(path)
            with open(path+ filename, 'wb') as file:
                file.write(resp.content)
                print('[INFO] 保存%s成功' % filename)
        except Exception as e:
            print(e)
            print('[INFO]保存失败的图片地址:%s '%img)
def main():
    #choose()函数的返回值是用户选择的图片检索方式对应的链接 返回值是一个元组类型 (url,name)
    tuple_=choose()
    url=tuple_[0]
    name=tuple_[1]
    #创建页面链接队列和图片链接队列
    PageQueue=Queue(100)
    ImgQueue=Queue(1000)
    start=int(input("输入开始页数："))
    end=int(input("输入结束页数："))
    for i in range(start,end):
        page_url=url+'&page='+str(i)
        #存到队列
        PageQueue.put(page_url)
    #设置线程数量
    for i in range(5):
        t1=GetImgUrl(PageQueue,ImgQueue)
        t1.start()
    for i in range(5):
        t2=DownloadImg(ImgQueue,name)
        t2.start()
if __name__ == '__main__':
    main()
