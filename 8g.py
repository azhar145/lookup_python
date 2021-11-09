import os,csv,pandas as pd

b=os.listdir('/home/az2/Downloads/bb33')


g=pd.DataFrame()
for x in b:
    t=pd.read_csv('/home/az2/Downloads/bb33/' + x)
    g=g.append(t)

g1=g
print(g1.shape,g.shape)
