import os;import pandas as pd
from faker import Faker
fake=Faker()


d1=[];d2=[];d3=[];d4=[]
for x in range(40):
    d1.append(fake.name())
    d2.append(fake.address())
    d3.append(fake.job())
    d4.append(fake.state())
    f=pd.DataFrame([d1,d2,d3,d4])

f=f.T
#print(f)
f.set_axis(['name','address','job','state'],axis=1,inplace=True)
print(f[['state']].value_counts())

