import os;import pandas as pd;
from faker import Faker
fake=Faker()

d1=[];d2=[]

for x in range(5):
    d1.append(fake.state())
    d2.append(fake.name())

    df=pd.DataFrame([d1,d2])

df1=df.T
print(df1)
df1.to_csv('/home/az2/Downloads/'
