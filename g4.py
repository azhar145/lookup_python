import os;import pandas as pd
from faker import Faker
fake=Faker()

d1=[];d2=[];d3=[];d4=[]
for x in range(20):
    d1.append(fake.name())
    d2.append(fake.address())
    d3.append(fake.job())
    d4.append(fake.state())
    g=pd.DataFrame([d1,d2,d3,d4])

g=g.T
g.set_axis(['name','address','job','state'],axis=1,inplace=True)
print(g.head(2))
print(g['state'].value_counts())
##print(g.loc[~g['state'].isin('Maryland')])
