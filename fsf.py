import pandas as pd;import os

f=os.listdir('/home/az2/Downloads/bb33/')


df=pd.DataFrame()

for x in f:
    g=pd.read_csv('/home/az2/Downloads/bb33/' + x )
##    print(g.head(2))
    df=df.append(g)
##    print(df)

print(df.count())    
    
    
