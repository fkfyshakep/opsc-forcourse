# install lxml

import requests
import random
from lxml import etree
def main():
    #proxies_test()
    test2()

def test2():
    url='https://movie.douban.com/review/14107342/'
    try:
        req=requests.get(url,headers=random_ua(),timeout=100)
        rsp=req.content
        htmls=etree.HTML(rsp)
        result=etree.tostring(htmls,encoding='utf-8').decode('utf-8')
        saves(result)
    except Exception as e:
        print("Error:",e)


def setkwd():
    need=False
    str=''
    if(need):
        str=input("输入你要查询的信息:")   
    kwd={
        'wd':str
    }
    return kwd

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

def random_ip():
    ip_list=[
        # 代理IP：https://ip.jiangxianli.com/?page=1
        # 注意：许多IP不一定可用，使用前建议测试一下http://httpbin.org/get
        # ==========非高匿或不可用list==========
        #
        # ===============可用list===============
        '120.34.194.172:7082',
        # ==============测试区list==============
        #
    ]
    temp=random.choice(ip_list)
    ips={
        'http':'http://'+temp,
        'https':'https://'+temp
    }
    print('\n'+'选择了IP:\t'+temp+'\n')
    return ips

def proxies_test():
    url='http://httpbin.org/get'
    try:
        #resp=requests.get(url,proxies=random_ip(),headers=random_ua(),timeout=100,allow_redirects=False)
        resp=requests.get(url,headers=random_ua(),timeout=100,allow_redirects=False)
        if(resp.status_code==200):
            text=resp.content.decode('utf-8')
            print(text)
    except Exception as e:
        print("Error:",e)

def saves(filename):
    str=input("输入文件名|带后缀：")
    str='opsc2/opsc2r/'+str
    with open(str,mode='w',encoding='utf-8') as f:
        f.write(filename)
    print('save,end!\n')

if __name__=='__main__':
    main()






