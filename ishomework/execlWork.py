
import pandas as pd
data = []
data = pd.read_csv(r"islist0.csv", sep=',', header='infer')
dataframe=pd.DataFrame(data)
dataframe.to_excel('test.xls', header=['简介', '地址', '位置', '房屋详细信息', '价格', '关注人数/发布时间'])

