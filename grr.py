import os;import pandas as pd

g=os.listdir('/home/az2/Downloads/bb33/')

d1=pd.DataFrame()
d2=pd.DataFrame()
k=0
for x in g:
    k=k+1
    p=pd.read_csv('/home/az2/Downloads/bb33/' + str(x))
    d2=d1.append(p)

print(k,'   ',d2.shape)    
