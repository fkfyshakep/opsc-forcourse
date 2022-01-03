# https://bj.lianjia.com/ershoufang/
# 对上方的二手房网站爬取
# 团子 

import requests
import random
from lxml import etree
import csv
import time
# 随机UA函数
def random_ua():
    ua_list = [
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Maxthon 2.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_0) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11',
    'Mozilla/5.0 (Windows NT 6.1; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0)',
    'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0',
    'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1',
    ]
    kw={
        'User-Agent':random.choice(ua_list)
    }
    return kw

# XPath匹配和输出函数(其中，html为content值)
def xfind(html,xpaths):
    # 初步解析函数与解码
    ans_list=html.xpath(xpaths)
    # print(ans)
    item={}
    for ans in ans_list:
        # 处理字典数据，注意xpath表达式匹配结果是一个列表，因此需要索引[0]提取数据.strip()
        # //*[@id="content"]/div/ul/li
        # title:    .//div/div/a/text()
        # location[1,2]:    .//div/div/div[@class="positionInfo"]/a[1]/text()   .//div/div/div[@class="positionInfo"]/a[2]/text()
        # status:   .//div/div/div[@class='houseInfo']/text()
        # price:    .//div/div[@class="unitPrice"]/span/text()
        # 注意price与location为list
        item['title']=ans.xpath('.//div/div/a/text()')[0].strip()
        item['locationa']=ans.xpath('.//div/div/div[@class="positionInfo"]/a[1]/text()')[0].strip()
        item['locationb']=ans.xpath('.//div/div/div[@class="positionInfo"]/a[2]/text()')[0].strip()
        item['square']=ans.xpath('.//div/div/div[@class="houseInfo"]/text()')[0].strip()
        item['price']=ans.xpath('.//div/div[@class="unitPrice"]/span/text()')[0].strip()
        item['follow']=ans.xpath('.//div/div[@class="followInfo"]/text()')[0].strip()
        # svs(lists)
        # 输出数据
        print(item)
        svs(item)

# 计数器
counternumber=0
def svs(filename):
    with open('opsc4/resources_4/lis0.csv',mode='a',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['title','locationa','locationb','square','price','follow'])
        # writer.writeheader()
        writer.writerow(filename)
        global counternumber
        counternumber+=1
        print('end!')

def testcounter():
    global counternumber
    counternumber+=2
    print(counternumber)

def run(url):
    try:
        req=requests.get(url=url,headers=random_ua(),timeout=200).text
        # resp=req.content
        texts=etree.HTML(req)
        # 初步解析
        xfind(texts,'//*[@id="content"]/div/ul/li')
    except Exception as e:
        print('Error:',e)

def testrun():
    url='https://bj.lianjia.com/ershoufang/'
    strs='pg'
    for i in range(1,2):
        urls=url+strs+str(i)+'/'
        run(urls)
        time.sleep(4)

def main():
    testrun() 
    testcounter()

if __name__=='__main__':
    main()

