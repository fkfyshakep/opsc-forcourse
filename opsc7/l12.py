# 细化分组，去除不必要的数据
# 顾余九逝魂，与子各何之；我歌诚自恸，非独为君悲
import pandas
import csv
import string
import re
# 数据读取测试
def tst():
    '''
    advertistitle    格局方正 采光好 保持的很干净 业主自住
    locationa                     新华联家园南区
    locationb                          果园
    configs                         3室2厅#
    areas                       119.18平米#
    directs                        南 西 北
    decorates                         精装
    floors                      中楼层(共7层)#
    evers                         2002年建#
    typs                               板楼
    price                       44,052元/平#
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
    runs(df)

def runs(df):
    for num in range(0,2400):
        # ['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
        lca=df.iloc[num]['locationa']#'locationa'
        lcb=df.iloc[num]['locationb']#'locationb'
        cfa,cfb=configs(df,num)
        cfa=str(cfa)#'configsa'
        cfb=str(cfb)#'configsb'
        ars=str(areas(df,num))#'areas'
        dcs=df.iloc[num]['decorates']#'decorates'
        fls=floors(df,num)#'floors'
        evs=str(evers(df,num))#'evers'
        tps=df.iloc[num]['typs']#'typs'
        pce=str(price(df,num))#'price'
        flwr=str(followers(df,num))#'followers'
        item={
            'locationa':lca,
            'locationb':lcb,
            'configsa':cfa,
            'configsb':cfb,
            'areas':ars,
            'decorates':dcs,
            'floors':fls,
            'evers':evs,
            'typs':tps,
            'price':pce,
            'followers':flwr
        }
        svs(item)

# save函数
def svs(filename):
    with open('opsc7\opsc7_r\isAnalys.csv',mode='a',encoding='utf-8',newline='') as f:
        writer=csv.DictWriter(f,delimiter='$',fieldnames=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers'])
        # writer.writeheader()
        writer.writerow(filename)

# 针对followers的处理，返回一个int
def followers(aline,num):
    try:
        str_followers=aline.iloc[num]['followers']
        num=re.findall(r"\d+\.?\d*",str_followers)[0]
        num=int(num)
        return num
    except Exception as e:
        print('Error:',e)
        return 0

# 对建立年份evers的处理，返回一个int
def evers(aline,num):
    try:
        str_evers=aline.iloc[num]['evers']
        num=re.findall(r"\d+\.?\d*",str_evers)[0]
        num=int(num)
        return num
    except Exception as e:
        print('Error:',e)
        return 0

# 针对楼层的floors处理，返回string
def floors(aline,num):
    try:
        str_floors=aline.iloc[num]['floors']
        fl_list=str_floors.split('(')
        refl=fl_list[0]
        return refl
    except Exception as e:
        print('Error:',e)
        return ''

# 针对面积的areas的处理，正则表达式匹配 返回一个int
def areas(aline,num):
    try:
        str_areas=aline.iloc[num]['areas']
        num=re.findall(r"\d+\.?\d*",str_areas)[0]
        num=float(num)
        return num
    except Exception as e:
        print('Error:',e)
        return 0

# 针对configs的处理,返回两个值： a,b=configs()（int）
def configs(aline,num):
    str_configs=aline.iloc[num]['configs']
    try:
        conf_list=str_configs.split('室')
        conf_list1=conf_list[0].strip()
        conf_list=conf_list[1].strip()
        conf_list2=conf_list[0]
        intshi=int(conf_list1)
        intting=int(conf_list2)
        return intshi,intting
    except Exception as e:
        print('Error:',e)
        return 0,0

# 针对price的处理,两个参数：示例(df=read_cvs,1)
def price(aline,num):
    str_price=aline.iloc[num]['price']
    try:
        price_list=str_price.split(',')
        int_left=int(price_list[0])# 前
        int_right=int(price_list[1][0:3])# 后
        ana_price=int_left*1000+int_right
        return ana_price
    except Exception as e:
        print('Error:',e)
        return 0

def main():
    tst()

if __name__=='__main__':
    main()       