import os;import pandas as pd
from faker import Faker
fake=Faker()

d1=[];d2=[];d3=[]
for x in range(600):
    d1.append(fake.name())
    d2.append(fake.job())
    d3.append(fake.state())
    df=pd.DataFrame([d1,d2,d3])

df=df.T
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 22)

df.set_axis(['name','job','state'],axis=1,inplace=True)
##df1=df.iloc[65:83,0:4]  
##df2=df.iloc[0:78,0:4]

##g=pd.merge(df1,df2,left_on='state',right_on='state',how='outer')
##g1=pd.merge(df1,df2,left_on='state',right_on='state',how='left')
g1=df.pivot(index='job',columns='state',values='name')
print(g1)

