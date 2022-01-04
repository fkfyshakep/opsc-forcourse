# 数据可视化
# 流萤漫天花共舞，闲蝉栖柳风奏湖
# pip install pyecharts
import pyecharts
import pandas
import csv
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams['font.sans-serif'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False 
# plt.rcParams['savefig.dpi'] = 400 #图片像素
plt.rcParams['figure.dpi'] = 300 #分辨率
font2 = {'color':'darkred','size':5}
# 数据读取测试
def tst():
    fname='opsc7\opsc7_r\isAnalys.csv'
    binding=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
    # pandas.set_option('display.max_columns', None)
    # row=skip+n all start in 0
    # fname,encoding='utf-8',header=None,skiprows=num,nrows=1,usecols=[0]
    # df.iloc[0]['title']
    df = pandas.read_csv(fname,encoding='utf-8',names=binding,header=None,delimiter='$')
    runs(df)

# # 数组和
# fieldnames=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
def listca(df,strs):
    li=[]
    #               0           1           2           3       4           5       6       7       8       9       0
    fieldnames=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
    lca=None
    if (strs==fieldnames[0] or strs==fieldnames[1] or strs==fieldnames[5] or strs==fieldnames[6] or strs==fieldnames[8]):
        for num in range(0,2400):
            lca=df.iloc[num][strs]
            li.append(lca)
    elif (strs==fieldnames[2] or strs==fieldnames[3] or strs==fieldnames[7] or strs==fieldnames[9] or strs==fieldnames[10]):
        for num in range(0,2400):
            lca=df.iloc[num][strs]
            if(lca==''):
                lca=0
            else:
                lca=int(lca)
            li.append(lca)
    elif (strs==fieldnames[4]):
        for num in range(0,2400):
            lca=df.iloc[num][strs]
            if(lca==''):
                lca=0
            else:
                lca=float(lca)
            li.append(lca)
    return li

# 楼房类型 分布 板楼塔楼，板塔楼结合，其它
def typstest(df):
    li=listca(df,strs='typs')
    numb=0
    numc=0
    numd=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 板楼'):
            numb+=1
        elif(li[num]==' 塔楼'):
            numc+=1
        elif(li[num]==' 板塔结合'):
            numd+=1
        else:
            others+=1
    xlist=[' 板楼',' 塔楼',' 板塔结合',' 其他']
    ylist=[numb,numc,numd,others]
    plt.barh(xlist, ylist)  # 横放条形图函数 barh
    plt.title('楼房类型分布')
    plt.savefig('opsc7\photos\ps1.png',dpi = 400)
    plt.show()

def typstest2(df):
    li=listca(df,strs='typs')
    numb=0
    numc=0
    numd=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 板楼'):
            numb+=1
        elif(li[num]==' 塔楼'):
            numc+=1
        elif(li[num]==' 板塔结合'):
            numd+=1
        else:
            others+=1
    xlist=[' 板楼',' 塔楼',' 板塔结合',' 其他']
    numb=numb/2400
    numc=numc/2400
    numd=numd/2400
    others=1-numb-numc-numd
    pslist=[numb,numc,numd,others]
    ylist=np.array(pslist)
    plt.pie(ylist,labels=xlist,colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"])
    plt.title('楼房类型分布(饼状图)')
    plt.savefig('opsc7\photos\ps2.png',dpi = 400)
    plt.show()

# v1.0
def areatest1(df):
    li=listca(df,strs='areas')
    # 50 70 90 110 130 150
    num1=0
    num2=0
    num3=0
    num4=0
    num5=0
    num6=0
    num7=0
    num0=0
    for num in range(0,2400):
        if(li[num]==0):
            num0+=1
        elif(li[num]<50.0 and li[num]>0):
            num1+=1
        elif(li[num]>=50.0 and li[num]<70.0):
            num2+=1
        elif(li[num]>=70.0 and li[num]<90.0):
            num3+=1
        elif(li[num]>=90.0 and li[num]<110.0):
            num4+=1
        elif(li[num]>=110.0 and li[num]<130.0):
            num5+=1
        elif(li[num]>=130.0 and li[num]<150.0):
            num6+=1
        else:
            num7+=1
    xlist=['未知','0~50','50~70','70~90','90~110','110~130','130~150','>150']
    ylist=[num0,num1,num2,num3,num4,num5,num6,num7]
    plt.barh(xlist, ylist)  # 横放条形图函数 barh
    plt.title('楼房面积分布(柱状图)')
    plt.savefig('opsc7\photos\ps3.png',dpi = 400)
    plt.show()

# 楼房面积改进版
# 参考:https://stackoverflow.com/questions/23944657/typeerror-method-takes-1-positional-argument-but-2-were-given
def areatest2(df):
    li=listca(df,strs='areas')
    numlist=[]
    counters=0
    c1=0
    c2=0
    # 50--70--90--110--130--150
    for num in range(0,2400):
        if li[num]<=50:
            c1+=1
        elif li[num]>200:
            c2+=1
        else:
            continue
    numlist.append(c1)
    for s in range(50,200,10):
        counters=0
        for num in range(0,2400):
            if(li[num]>s and li[num]<=(s+10)):
                counters+=1
            else:
                continue
        numlist.append(counters)
    numlist.append(c2)
    xlist=['0~50','50~60','60~70','70~80','80~90','90~100','100~110','110~120','120~130','130~140','140~150','150~160','160~170','170~180','180~190','190~200','>200']
    resp=plt.bar(xlist, numlist,0.5,edgecolor='grey',alpha=0.8)  # 横放条形图函数 barh
    plt.title('楼房面积分布(柱状图2)')
    ##############################设置xy轴字体大小
    plt.xticks(fontproperties = 'Times New Roman', size = 4)
    plt.yticks(fontproperties = 'Times New Roman', size = 5)
    ##############################设置数据标签
    for a,b in zip(xlist,numlist):
        plt.text(a,b,b,ha='center',va='bottom',fontsize=6)
    ##############################
    plt.savefig('opsc7\photos\ps4.png',dpi = 400)
    plt.show()
    '''
    advertistitle    格局方正 采光好 保持的很干净 业主自住
    locationa                     新华联家园南区
    locationb                          果园
    configs                         3室2厅
    areas                       119.18平米#
    directs                        南 西 北
    decorates                         精装
    floors                      中楼层(共7层)
    evers                         2002年建
    typs                               板楼#
    price                       44,052元/平
    followers                      47人关注
    publish                       1个月以前发布
    '''
# 楼房类型 分布 板楼塔楼，板塔楼结合，其它
def decoratetest(df):
    li=listca(df,strs='decorates')
    numb=0
    numc=0
    numd=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 精装 '):
            numb+=1
        elif(li[num]==' 简装 '):
            numc+=1
        elif(li[num]==' 毛坯 '):
            numd+=1
        else:
            others+=1
    xlist=[' 精装',' 简装',' 毛坯',' 其他']
    ylist=[numb,numc,numd,others]
    plt.barh(xlist, ylist)  # 横放条形图函数 barh
    plt.title('楼房装饰方式分布(条形图)')
    plt.savefig('opsc7\photos\ps5.png',dpi = 400)
    plt.show()

def decoratetest2(df):
    li=listca(df,strs='decorates')
    numb=0
    numc=0
    numd=0
    others=0
    for num in range(0,2400):
        if(li[num]==' 精装 '):
            numb+=1
        elif(li[num]==' 简装 '):
            numc+=1
        elif(li[num]==' 毛坯 '):
            numd+=1
        else:
            others+=1
    xlist=[' 其他',' 精装',' 简装',' 毛坯']
    numb=float(format(numb/2400,'.2f'))
    numc=float(format(numc/2400,'.2f'))
    numd=float(format(numd/2400,'.2f'))
    others=(1-numb-numc-numd)
    pslist=[others,numb,numc,numd]
    # xlists=[xlist[0]+str(others*100)[0]+str(others*100)[1]+str(others*100)[2]+str(others*100)[3]+'%',xlist[1]+str(numb*100)[0]+str(numb*100)[1]+str(numb*100)[2]+str(numb*100)[3]+'%',xlist[2]+str(numc*100)[0]+str(numc*100)[1]+str(numc*100)[2]+str(numc*100)[3]+'%',xlist[3]+str(numd*100)[0]+str(numd*100)[1]+str(numd*100)[2]+str(numd*100)[3]+'%']
    ylist=np.array(pslist)
    plt.pie(ylist,labels=xlist,colors=["#d5695d", "#5d8ca8", "#65a479", "#a564c9"])
    plt.title('楼房装饰方式分布(饼状图)')
    plt.savefig('opsc7\photos\ps6.png',dpi = 400)
    plt.show()

# 在runs中修改调用的函数名，以调用不同函数
# fieldnames=['locationa','locationb','configsa','configsb','areas','decorates','floors','evers','typs','price','followers']
def runs(df):
    decoratetest2(df)
    
def main():
    tst()

if __name__=='__main__':
    main()