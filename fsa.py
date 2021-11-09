
    
    
import os; from faker import Faker;import pandas as pd
fake=Faker()

p=os.listdir('/home/az2/Downloads/bb33')
df=pd.DataFrame()
d1=[];d2=[]
for x in range(44):
    d1.append(fake.country())
    d2.append(fake.bank())
    df=pd.DataFrame([d1,d2])
    df=df.T
    df2=df.append(df)
    
print(df2)

    
