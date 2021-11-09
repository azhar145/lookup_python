import os;import pandas as pd
from faker import Faker
fake=Faker()


d1=[];d2=[];d3=[]
for x in range(400):
    d1.append(fake.name())
    d2.append(fake.state())
    d3.append(fake.text())
    df=pd.DataFrame([d1,d2,d3])

df=df.T
df.set_axis(['job','state','da'],axis=1,inplace=True)
##print(df.loc[(df['state'] == 'Wisconsin')])
##print(df[['state','da']])
print(df.iloc[0:20,:])
print(df['da'].value_counts())
