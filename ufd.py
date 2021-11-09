import os;import pandas as pd
from faker import Faker
fake=Faker()

d1=[];d2=[]

for x in range(33):
    d1.append(fake.state())
    d2.append(fake.name())
    df=pd.DataFrame([d1,d2])
    

df=df.T
print(df.shape)
print(df.head(5))
