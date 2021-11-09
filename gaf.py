import  pandas as pd
import os,csv

g=os.listdir('/home/az2/Downloads/bb33')

gm=pd.DataFrame()
for x in g:
    t=pd.read_csv('/home/az2/Downloads/bb33/' + x)
    gm=gm.append(t)

print(gm.shape)    
