#import urllib.request
##import re
import pandas as pd

def b():
    f1=open('/home/az2/Downloads/python_66/a/a1.txt','r')
    g=f1.readlines()

    m='azhar'
    n='idno'

    df1=pd.DataFrame(columns=['m','pa'])
    df2=pd.DataFrame(columns=['m','pb'])
    k=0 
    for x in g:
        
        k=k+1
        if (m in x):
            
            t1=x.index(m,0)

            sa1=x[t1:t1+12]
            df1=df1.append({'m':k,'pa':sa1},ignore_index=True)
##            print(k,',',sa1)

        if (n in x):
            
            t2=x.index(n,0)

            sa2=x[t2:t2+6]
            df2=df2.append({'m':k,'pb':sa2},ignore_index=True)
##            print(k,',',sa2)    
##    print(df1)
##    print(df2)
    
    g=pd.merge(df1,df2,on='m',how='outer')
    print(g)
    
    #######################################



b()
##print(df1)
