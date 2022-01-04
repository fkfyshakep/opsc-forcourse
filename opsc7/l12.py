# 细化分组，去除不必要的数据
# 
import pandas
import csv
import string
# 数据读取测试
def tst():
    '''
    advertistitle    格局方正 采光好 保持的很干净 业主自住
    locationa                     新华联家园南区
    locationb                          果园
    configs                         3室2厅
    areas                       119.18平米
    directs                        南 西 北
    decorates                         精装
    floors                      中楼层(共7层)
    evers                         2002年建
    typs                               板楼
    price                       44,052元/平
    followers                      47人关注
    publish                       1个月以前发布
    '''
    fname='opsc7\opsc7_r\isSplited.csv'
    binding=['advertistitle','locationa','locationb','configs','areas','directs','decorates','floors','evers','typs','price','followers','publish']
    # pandas.set_option('display.max_columns', None)
    # row=skip+n all start in 0
    # fname,encoding='utf-8',header=None,skiprows=num,nrows=1,usecols=[0]
    # df.iloc[0]['title']
    df = pandas.read_csv(fname,encoding='utf-8',names=binding,header=None,delimiter='$')
    print(df.iloc[0])
    print(df.iloc[0]['configs'])
    print(df.iloc[0]['configs'][0]+df.iloc[0]['configs'][2])


# 针对price的处理
def price(aline,num):
    str_price=aline.iloc[num]['price']
    price_list=str_price.split(',')
    int_left=int(price_list[0])
    int_right=int(price_list[1][0:3])
    ana_price=int_left*1000+int_right
    return ana_price

def main():
    tst()

if __name__=='__main__':
    main()       