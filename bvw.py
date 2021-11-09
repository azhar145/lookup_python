import os;import pandas as pd

g=os.listdir('/home/az2/Downloads/bb33/')
pd.set_option('display.max_colwidth', 10)
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 7)

df=pd.DataFrame()
df2=pd.DataFrame()
for x in g:
    print(x)
    x1=pd.read_csv('/home/az2/Downloads/bb33/'+x)
    print(x1)
    df2=df2.append(x1)

print(df2.shape,'   ', df2.size)    
print(df2)
