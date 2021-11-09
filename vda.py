import pandas as pd;from faker import Faker;import os

g=os.listdir('/home/az2/Downloads/bb33')


df2=pd.DataFrame()
k=0
for x in g:
    p=pd.read_csv('/home/az2/Downloads/bb33/' + x)
    df2=p.append(p)
    k=k+1

##
df2=df2.T
print(k)
print(df2.size,df2.shape)
print(df2.head(3))
