import pandas as pd;import os

b=os.listdir('/home/az2/Downloads/bb33/')


df=pd.DataFrame()
for x in b:
    m=pd.read_csv('/home/az2/Downloads/bb33/' + x)
    print(df.size)
    df=df.append(m)
    print(df.shape,x)
pd.set_option("display.max_rows",580)
pd.set_option("display.max_columns",580)
df2=df.iloc[0:300,1:2]
df3=df.iloc[0:100,1:2]
s=pd.merge(df2,df3, on=[1,1], how='outer')



print(df2.shape, df2)
