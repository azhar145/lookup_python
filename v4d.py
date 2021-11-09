import pandas as pd; import os
from faker import Faker
fake=Faker()

d1=[];d2=[]

##df=pd.DataFrame()
for x in range (4):
    d1.append(fake.state())
    d2.append(fake.city())
    df=pd.DataFrame([d1,d2])
df=df.T
print(df)    

df.to_csv('/home/az2/Downloads/bb33/' + str('_820'))
