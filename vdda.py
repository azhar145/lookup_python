
    
import os;import pandas as pd
from faker import Faker
fake=Faker()
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 11)

d1=[];d2=[];d3=[];d4=[];d5=[];d6=[]

for x in range(4):
    d1.append(fake.state())
    d2.append(fake.name())
    d3.append(fake.currency_code())
    d4.append(fake.job())
    d5.append(fake.date_of_birth())
    d6.append(fake.latlng())
    df=pd.DataFrame([d1,d2,d3,d4,d5])

df=df.T

df1=df.append(df)
df1.set_axis(['a1','a2','a3','a4','a5'], axis=1,inplace=True) 
##print(df1)
df2=df1.iloc[2:13,:]
print(df2)

print(df2.size,'   ',df2.shape)
print(df1.size,'  ',df1.shape)

g=pd.merge(df1,df2,on=['a2','a2'],how='inner')
print(g)

##    df1.to_csv('/home/az2/Downloads/bb33/' + '_blue_' + str(k))
##
##
##
##for k in range(33):
##    m(k)
