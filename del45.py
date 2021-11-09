import pandas as pd;import os

g=os.listdir('/home/az2/Downloads/bb33')

df2=pd.DataFrame()
for x in g:
    df1=pd.read_csv('/home/az2/Downloads/bb33/'+x)
    df2=df2.append(df1)


print(df2.count())    
