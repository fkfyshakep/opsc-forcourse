# 文件处理opsc5\opsc5_r\islist0.csv
# 醉看轻羽浮世去，此梦依稀落九黎。
# pip install pandas
# pip list

import pandas
import csv

def tst():
    fname='opsc5\opsc5_r\islist0.csv'
    binding=['title','locationa','locationb','square','price','follow']
    # pandas.set_option('display.max_columns', None)
    # row=skip+n all start in 0
    df = pandas.read_csv(fname,encoding='utf-8',header=None,names=binding)
    print(df)

# 数据读取测试
def printtest():
    fname='opsc5\opsc5_r\islist0.csv'
    binding=['title','locationa','locationb','square','price','follow']
    # pandas.set_option('display.max_columns', None)
    # row=skip+n all start in 0
    df = pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=1,nrows=1,usecols=[3])
    # print(df)
    # df = pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=1,nrows=1,usecols=[4])
    # print(df)
    # df = pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=1,nrows=1,usecols=[5])
    print(df)
    text=str(df)
    ad=text.split('|',7)
    print(ad[5])

# # 表头添加测试
# def addheaders():
#     df = pandas.read_csv('opsc5\opsc5_r\islist0.csv',encoding='utf-8',header=None,names=['title','locationa','locationb','square','price','follow'])
#     df.csv('opsc5\opsc5_r\islist1.csv',index=False)
# 文件分割
def splits(num):
    fname='opsc5\opsc5_r\islist0.csv'
    binding=['title','locationa','locationb','square','price','follow']
    # row=skip+n all start in 0
    # 读取出来一行且分割的数据
    # 格局方正采光好保持的很干净业主自住,新华联家园南区,果园,3室2厅 | 119.18平米 | 南 西 北 | 精装 | 中楼层(共7层) | 2002年建 | 板楼,"44,052元/平",47人关注 / 1个月以前发布
    temp_title = pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=num,nrows=1,usecols=[0])
    temp_locationa=pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=num,nrows=1,usecols=[1])
    temp_locationb=pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=num,nrows=1,usecols=[2])
    temp_square=pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=num,nrows=1,usecols=[3])
    temp_price=pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=num,nrows=1,usecols=[4])
    temp_follow=pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=num,nrows=1,usecols=[5])
    text_title=str(temp_title)#none
    text_locationa=str(temp_locationa)#none
    text_locationb=str(temp_locationb)#none
    text_square=str(temp_square)#configs areas directs decorates floors evers typs
    text_price=str(temp_price)#none
    text_follow=str(temp_follow)#followers days
    squares=text_square.split('|')#list
    follows=text_follow.split('/')#list
    transave(text_title,text_locationa,text_locationb,squares,text_price,follows)

#特别的保存函数
def transave(title,locationa,locationb,squarelist,price,followlist):
    item={}
    # ['advertistitle','locationa','locationb','configs','areas','directs','decorates','floors','evers','typs','price','followers','publish']
    item['advertistitle']=title
    item['locationa']=locationa
    item['locationb']=locationb
    # squarelists
    try:
        item['configs']=squarelist[0]
    except Exception as e:
        print('0 is null')
        item['configs']=''
    try:
        item['areas']=squarelist[1]
    except Exception as e:
        print('1 is null')
        item['areas']=''
    try:
        item['directs']=squarelist[2]
    except Exception as e:
        print('2 is null')
        item['directs']=''
    try:
        item['decorates']=squarelist[3]
    except Exception as e:
        print('3 is null')
        item['decorates']=''
    try:
        item['floors']=squarelist[4]
    except Exception as e:
        print('4 is null')
        item['floors']=''
    try:
        item['evers']=squarelist[5]
    except Exception as e:
        print('5 is null')
        item['evers']=''
    try:
        item['typs']=squarelist[6]
    except Exception as e:
        print('6 is null')
        item['typs']=''
    item['price']=price
    # followlists
    try:
        item['followers']=followlist[0]
    except Exception as e:
        print('8 is null')
        item['followers']=''
    try:
        item['publish']=followlist[1]
    except Exception as e:
        print('9 is null')
        item['publish']=''
    svs(item)

def svs(filename):
    with open('opsc5\opsc5_r\istransforms.csv',mode='a',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,delimiter='$',fieldnames=['advertistitle','locationa','locationb','configs','areas','directs','decorates','floors','evers','typs','price','followers','publish'])
        # writer.writeheader()
        writer.writerow(filename)

# 运行文件处理
def runs():
    # for i in range(0,2):0,1
    for i in range(0,2400):
        splits(i)

def main():
    runs()

if __name__=='__main__':
    main()    