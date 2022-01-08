# -*- coding: utf-8 -*-
# @Time: 2021/12/31 19:49
# @File : choose.py
from urllib import parse

def choose():
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
        name=category_name(category_id)
        print("你选择的类别是%s" % name)
        category_url = category + str(category_id) + "&lang=Chinese"
        print(category_url)
        return category_url,name
    elif search == 2:
        search_ = "https://wall.alphacoders.com/search.php?search="
        key = input("输入你要获取的壁纸关键字：")
        key_ = parse.quote(key)
        search_url = search_ + key_ + "&lang=Chinese"
        print(search_url)
        return search_url,key
    else:
        print("看清楚提示，哈麻皮！！！")
def category_name(name):
    if name == 1:
        category_name='抽象'
        return category_name
    if name == 2:
        category_name= '动物'
        return category_name
    if name == 3:
        category_name=  '动漫'
        return category_name
    if name == 4:
        category_name=  '艺术'
        return category_name
    if name == 5:
        category_name=  '名人'
        return category_name
    if name == 6:
        category_name=  '漫画'
        return category_name
    if name == 7:
        category_name=  '黑暗'
        return category_name
    if name == 8:
        category_name=  '自然'
        return category_name
    if name == 9:
        category_name=  '奇幻'
        return category_name
    if name == 10:
        category_name=  '食物'
        return category_name
    if name == 11:
        category_name=  '游戏'
        return category_name
    if name == 12:
        category_name=  '节日'
        return category_name
    if name == 13:
        category_name=  '幽默'
        return category_name
    if name == 14:
        category_name=  '人造'
        return category_name
    if name == 15:
        category_name=  '人局'
        return category_name
    if name == 16:
        category_name=  '军事'
        return category_name
    if name == 17:
        category_name=  '综合'
        return category_name
    if name == 18:
        category_name=  '电影'
        return category_name
    if name == 19:
        category_name=  '音乐'
        return category_name
    if name == 20:
        category_name=  '摄影'
        return category_name
    if name == 21:
        category_name=  '产品'
        return category_name
    if name == 22:
        category_name=  '宗教'
        return category_name
    if name == 23:
        category_name=  '科幻'
        return category_name
    if name == 24:
        category_name=  '运动'
        return category_name
    if name == 25:
        category_name=  '艺术'
        return category_name
    if name == 26:
        category_name=  '电视'
        return category_name
    if name == 27:
        category_name=  '座驾'
        return category_name
    if name == 28:
        category_name=  '游戏'
        return category_name
    if name == 29:
        category_name=  '武器'
        return category_name
    if name == 30:
        category_name=  '女性'
        return category_name


