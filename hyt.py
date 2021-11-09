import os;import pandas as pd
from faker import Faker
fake=Faker()

pd.set_option('display.max_rows', 590)
pd.set_option('display.max_columns', 5)

d1=[];d2=[];d3=[];d4=[]

for x in range (30):
    d1.append(fake.name())
    d2.append(fake.address())
    d3.append(fake.bank_country())
    d4.append(fake.job())
    df=pd.DataFrame([d1,d2,d3,d4])

df=df.T
##df.set_axis(['a1','a2','a3','a4'], axis=1,inplace=True) 

print(df.filter(regex='A$', axis=1))    
