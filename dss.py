import pandas as pd;import os
g=os.listdir('/home/az2/Downloads/bb33')


df=pd.DataFrame()
for x in g:
    f=pd.read_csv('/home/az2/Downloads/bb33/' + x)
    df=df.append(f)

print(df.count())    
