import requests
import random
from lxml import etree
import csv
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

# Params传参设定函数
def setkwd(offset):
    need=False
    str='bdacc9c7e0c37c67c9833370244d23f2lvssf'
    if(need):
        str=input("输入你要查询的信息:")   
    kwd={
        'requestCode':str,
        'offset':offset,
    }
    return kwd

# XPath匹配和输出函数(其中，html为content值)
def xfind(html,xpaths):
    # 解析函数与解码
    ans_list=html.xpath(xpaths)
    # print(ans)
    item={}
    for ans in ans_list:
        # 处理字典数据，注意xpath表达式匹配结果是一个列表，因此需要索引[0]提取数据.strip()
        # a=ans.xpath('.//div/div/div/p[1]/a')[0]
        # b=ans.xpath('.//div/div/div/p[2]')[0]
        # c=ans.xpath('.//div/div/div/p[3]')[0]
        # name=etree.tostring(a,encoding='utf-8').decode('utf-8','ignore')
        # star=etree.tostring(b,encoding='utf-8').decode('utf-8','ignore')
        # timp=etree.tostring(c,encoding='utf-8').decode('utf-8','ignore')
        # lists=[name,star,timp]
        item['name']=ans.xpath('.//p[@class="name"]/a/text()')[0].strip()
        item['star']=ans.xpath('.//p[@class="star"]/text()')[0].strip()
        item['time']=ans.xpath('.//p[@class="releasetime"]/text()')[0].strip()
        # svs(lists)
        # 输出数据
        print(item)
        svs(item)


# //*[@id="app"]/div/div/div/dl/dd
# //*[@id="app"]/div/div/div/dl/dd/div/div/div/p[2]   主演:
# //*[@id="app"]/div/div/div/dl/dd/div/div/div/p[3]   时间:
# //*[@id="app"]/div/div/div/dl/dd/div/div/div/p[1]/a 名字:

def svs(filename):
    with open('opsc3/opsc3_r/lis2.csv',mode='a',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,fieldnames=['name','star','time'])
        # writer.writeheader()
        writer.writerow(filename)
        print('end!')

def run():
    url='https://www.maoyan.com/board/4'
    try:
        req=requests.get(url=url,params=setkwd('0'),headers=random_ua(),timeout=200).text
        # resp=req.content
        texts=etree.HTML(req)
        xfind(texts,'//*[@id="app"]/div/div/div/dl/dd')
    except Exception as e:
        print('Error:',e)

def main():
    run() 

if __name__=='__main__':
    main()