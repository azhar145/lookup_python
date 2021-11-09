import os;import pandas as pd
from faker import Faker
fake=Faker()


d1=[];d2=[];d3=[]

for x in range(144):
    d1.append(fake.state())
    d2.append(fake.name())
    d3.append(fake.job())
    df=pd.DataFrame([d1,d2,d3])
df=df.T
##print(df.iloc[20:35, 0:2])    
df1=df.iloc[0:100, 0:3]
##df2=df.iloc[25:55, 0:2]
df1.set_axis(['state_1','name','nno'],axis=1,inplace=True)
##df2.set_axis(['state_2','y'],axis=1,inplace=True)
##print(df1.head(2))
##print(df2.head(2))
##g=pd.merge(df1,df2,left_on='x',right_on='y',how='outer')
##print(g)
##g=pd.merge(df1,df2,left_on='x',right_on='y',how='inner')
##print(g)
##g=pd.merge(df1,df2,left_on='x',right_on='y',how='left')
##print(g)
##g=pd.merge(df1,df2,left_on='x',right_on='y',how='right')
##print(g)
pp=df1.pivot(index='nno',columns='state_1',values='name')
print(pp)
