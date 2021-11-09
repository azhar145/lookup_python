import os;import pandas as pd
from faker import Faker
fake=Faker()

d1=[];d2=[];d3=[]

for x in range(300):
    d1.append(fake.name())
    d2.append(fake.state())
    d3.append(fake.job())
    df=pd.DataFrame([d1,d2,d3])


df.set_axis(['name','state','job'],axis=1, inplace=True)   
print(df.loc[(df['state'] == 'Wisconsin')])
print(df.iloc[:,[0,6,8]])
