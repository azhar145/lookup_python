import pandas as pd;import os

p=os.listdir('/home/az2/Downloads/bb33')


df1=pd.DataFrame()
for x in p:
    b=pd.read_csv('/home/az2/Downloads/bb33/'+x)
    df1=df1.append(b)

print(df2.count())    
