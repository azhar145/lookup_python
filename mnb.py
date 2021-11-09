import pandas as pd; import os

g=os.listdir('/home/az2/Downloads/bb33/')
pd.set_option("display.max_rows",580)
pd.set_option("display.max_columns",380)

d77=[]
df2=pd.DataFrame()
df3=pd.DataFrame()
k=0
for x in g:
##    print(x)
    d77.append(x)
    df1=pd.read_csv('/home/az2/Downloads/bb33/' + x )
    df2=df2.append(df1)
    df3=df3.append(df2,d77)
    k=k+1



print(k, ' files')
print(df3.shape)
