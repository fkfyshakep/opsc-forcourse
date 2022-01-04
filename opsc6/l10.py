import pandas
import csv

def tst():
    fname='opsc5\opsc5_r\islist0.csv'
    binding=['title','locationa','locationb','square','price','follow']
    # pandas.set_option('display.max_columns', None)
    # row=skip+n all start in 0
    # fname,encoding='utf-8',header=None,skiprows=num,nrows=1,usecols=[0]
    df = pandas.read_csv(fname,encoding='utf-8',names=binding,header=None)
    print(df.iloc[0]['title'])

# 数据读取测试
def printtest():
    fname='opsc6\opsc6_r\islist0.csv'
    binding=['title','locationa','locationb','square','price','follow']
    # pandas.set_option('display.max_columns', None)
    # row=skip+n all start in 0
    df = pandas.read_csv(fname,encoding='utf-8',header=None,names=binding,skiprows=1,nrows=1,usecols=[3])
    # print(df)
    # df = pandas.read_csv(fname,encoding='utf-8',header=None,skiprows=1,nrows=1,usecols=[4])
    # print(df)
    # df = pandas.read_csv(fname,encoding='utf-8',header=None,skiprows=1,nrows=1,usecols=[5])
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
    fname='opsc6\opsc6_r\islist0.csv'
    binding=['title','locationa','locationb','square','price','follow']
    openfile=pandas.read_csv(fname,encoding='utf-8',names=binding,header=None)
    # row=skip+n all start in 0
    # 读取出来一行且分割的数据
    # 格局方正采光好保持的很干净业主自住,新华联家园南区,果园,3室2厅 | 119.18平米 | 南 西 北 | 精装 | 中楼层(共7层) | 2002年建 | 板楼,"44,052元/平",47人关注 / 1个月以前发布
    temp_title = openfile.iloc[num]['title']
    temp_locationa=openfile.iloc[num]['locationa']
    temp_locationb=openfile.iloc[num]['locationb']
    temp_square=openfile.iloc[num]['square']
    temp_price=openfile.iloc[num]['price']
    temp_follow=openfile.iloc[num]['follow']
    # text_title=(temp_title.to_string())#none
    # text_locationa=(temp_locationa.to_string())#none
    # text_locationb=(temp_locationb.to_string())#none
    # text_square=(temp_square.to_string())#configs areas directs decorates floors evers typs
    # text_price=(temp_price.to_string())#none
    # text_follow=(temp_follow.to_string())#followers days
    squares=temp_square.split('|')#list
    follows=temp_follow.split('/')#list
    transave(temp_title,temp_locationa,temp_locationb,squares,temp_price,follows)

# 特别的分割函数
def transave(title,locationa,locationb,squarelist,price,followlist):
    # ['advertistitle','locationa','locationb','configs','areas','directs','decorates','floors','evers','typs','price','followers','publish']
    item_title=title
    item_locationa=locationa
    item_locationb=locationb
    # squarelists
    try:
        item_configs=squarelist[0]
    except Exception as e:
        print('configs is null')
        item_configs=''
    try:
        item_areas=squarelist[1]
    except Exception as e:
        print('1 is null')
        item_areas=''
    try:
        item_directs=squarelist[2]
    except Exception as e:
        print('2 is null')
        item_directs=''
    try:
        item_decorates=squarelist[3]
    except Exception as e:
        print('3 is null')
        item_decorates=''
    try:
        item_floors=squarelist[4]
    except Exception as e:
        print('4 is null')
        item_floors=''
    try:
        item_evers=squarelist[5]
    except Exception as e:
        print('5 is null')
        item_evers=''
    try:
        item_typs=squarelist[6]
    except Exception as e:
        print('6 is null')
        item_typs=''
    item_price=price
    # followlists
    try:
        item_followers=followlist[0]
    except Exception as e:
        print('8 is null')
        item_followers=''
    try:
        item_publish=followlist[1]
    except Exception as e:
        print('9 is null')
        item_publish=''
    # svs(item)
    item={
        'advertistitle':item_title,
        'locationa':item_locationa,
        'locationb':item_locationb,
        'configs':item_configs,
        'areas':item_areas,
        'directs':item_directs,
        'decorates':item_decorates,
        'floors':item_floors,
        'evers':item_evers,
        'typs':item_typs,
        'price':item_price,
        'followers':item_followers,
        'publish':item_publish
    }
    print(item)
    svs(item)

# v2.0
def svs(filename):
    with open('opsc6\opsc6_r\isends.csv',mode='a',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,delimiter='$',fieldnames=['advertistitle','locationa','locationb','configs','areas','directs','decorates','floors','evers','typs','price','followers','publish'])
        # writer.writeheader()
        writer.writerow(filename)
# v3.0
# def svs(filename):
#     pass


# 运行文件处理
def runs():
    # for i in range(0,2):0,1 range(0,2400)
    for i in range(0,2400):
        splits(i)

def main():
    runs()

if __name__=='__main__':
    main()    