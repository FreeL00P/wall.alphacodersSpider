# wall.alphacodersSpider
# 一、网页地址分析
 首先打开我们爬取的[网站](https://wall.alphacoders.com/)，在搜索框输入一个不存在的壁纸关键字，例如：![输入一个不存在的关键字](https://img-blog.csdnimg.cn/f087a1a4f33644ba9cee0acaf0c2cbc1.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAZnJlZWwwMHA=,size_20,color_FFFFFF,t_70,g_se,x_16)

**我们可以发现，网页跳转到了一个[新网页](https://wall.alphacoders.com/search.php?search=fdsgvhbjf)，** ![鼠标停留在文字上](https://img-blog.csdnimg.cn/f1f537ae89074703846630ebc7bff89f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAZnJlZWwwMHA=,size_20,color_FFFFFF,t_70,g_se,x_16)
**可得，该网站的不同类别有不同的对应链接（但不是按照顺序排的，中间缺少几个数据）**

# 二、获取不同类别的壁纸对应的链接：
只需在后面加上id就可以得到，不同的类别链接，“https://wall.alphacoders.com/by_category.php?id=”
## 1、根据输入的id，输出对应的链接：
````
def choose():
#这里的关键词查询在后面会写
    search = int(input("请输入壁纸查询方式 1·····类别模糊查询||2·····关键词查询"))
    if search == 1:
        category = "https://wall.alphacoders.com/by_category.php?id="
        print("[INFO]下面是序号所对应的壁纸类别：\n"
              "  1·····抽象   2·····动物   3·····动漫   4·····艺术   7·····名人   8·····漫画\n"
              "  9·····黑暗  10·····自然  11·····奇幻  12·····食物  13·····幽默  14·····游戏\n"
              " 15·····节日  16·····人造  17·····人类  18·····军事  19·····综合  20·····电影\n"
              " 22·····音乐  24·····摄影  25·····产品  26·····宗教  27·····科幻  28·····运动\n"
              " 29·····电视  30·····技术  31·····座驾  32·····游戏  33·····女性  34·····武器")
        category_id = int(input("请输入你想爬取的壁纸类别序号："))
        # 判断用户输入的数据是否正确
        while True:
            if category_id in range(1, 35):
                break
            else:
                print("看清楚提示，哈麻皮！！！")
                category_id = int(input("请输入你想爬取的壁纸类别序号："))
        #这是根据用户输入，输出类别的名字
        name=category_name(category_id)
        print("你选择的类别是%s" % name)
      
        # 在链接后面加上lang=Chinese 网页就可以变成中文
       category_url = category + str(category_id) + "&lang=Chinese" 
        print(category_url)
        return category_url,name
````
## 2、输入后在根据用户输入id输出对应的类别名称：
```
def category_name(name):
    if name == 1:
        category_name='抽象'
        return category_name
#没什么卵用 太长了不贴全部了 有需要去GitHub上复制
```
## 3、当然该网站也可以直接搜索关键词（不过好像，你想到的大部分关键词，都是跳转到什么的类别链接）：
````
#根据上面输入的代码 输入2 就运行下面的代码，在输入你想搜索的壁纸关键字
    elif search == 2:
    #这是关键字搜索的链接
        search_ = "https://wall.alphacoders.com/search.php?search="
        key = input("输入你要获取的壁纸关键字：")
        #对输入的数据进行转码
        key_ = parse.quote(key)
        search_url = search_ + key_ + "&lang=Chinese"
        print(search_url)
        return search_url,key
    else:
        print("看清楚提示，哈麻皮！！！")
````
## 

## 4、打开网页，分析源码，例如[动漫类别](https://wall.alphacoders.com/by_category.php?id=3&name=Anime+Wallpapers)![在这里插入图片描述](https://img-blog.csdnimg.cn/be1322837c4e43168aacbd7cfb0b7f3f.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAZnJlZWwwMHA=,size_20,color_FFFFFF,t_70,g_se,x_16)
# 三、获取每页的链接
## 1、点击下一页，查看网页链接变化，发现只是简单的增长：
![在这里插入图片描述](https://img-blog.csdnimg.cn/ae5ff3756bdb41b09e772c0c6b58a7d4.png)


## 2、编写代码，输出每页的地址：
```
def main():
    #choose()函数的返回值是用户选择的图片检索方式对应的链接 返回值是一个元组类型 (url,name)
    #我把前面的代码写在单独的一个文件里面了
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
```
## 四、获取每页所有的壁纸链接，并存入到队列：
**我觉得我注释已经写的很清楚了**
```
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
```
## 五、从队列中取出数据，对壁纸链接发送请求，下载到本地：
**记得改一下路径**
```
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
```
# 六、保存到本地的效果如图所示：
![](https://img-blog.csdnimg.cn/ba0c7265394d4b4c9c07ad8ebb58286e.png?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,shadow_50,text_Q1NETiBAZnJlZWwwMHA=,size_20,color_FFFFFF,t_70,g_se,x_16)
## [源码地址]()
