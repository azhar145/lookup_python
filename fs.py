import pandas as pd; import os


f=os.listdir('/home/az2/Downloads/bb33/')

df=pd.DataFrame()
for x in f:
##    print(x)
    p=pd.read_csv('/home/az2/Downloads/bb33/' + x )
##    print(p.head(2))
    df=df.append(p)
    df.T
print(df.count())    
