import os;import pandas as pd
from faker import Faker
fake=Faker()
d1=[];d2=[]

for x in range(300):
    d1.append(fake.state())
    d2.append(fake.city())

    df=pd.DataFrame([d1,d2])

df=df.T    
df.iloc[2:50,0:1]
print(df)
