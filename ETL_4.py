#import urllib.request
##import re
import pandas as pd
import os

def b():
    pu='/home/az2/Downloads/python_66/a/a1.txt'
    f1=open(pu,'r')
    g=f1.readlines()

    pu=os.path.splitext(pu)[0]
    m='azhar'
    n='idno'
##    c=os.path.basename(

    df1=pd.DataFrame(columns=['m','pa','h'])
    df2=pd.DataFrame(columns=['m','pb','h'])
    k=0 
    for x in g:
        
        k=k+1
        if (m in x):
            
            t1=x.index(m,0)

            sa1=x[t1:t1+12]
            df1=df1.append({'m':k,'pa':sa1,'h':pu},ignore_index=True)
##            print(k,',',sa1)

        if (n in x):
            
            t2=x.index(n,0)

            sa2=x[t2:t2+200].split()
            df2=df2.append({'m':k,'pb':sa2,'h':pu},ignore_index=True)
##            print(k,',',sa2)    
##    print(df1)
##    print(df2)
    
    g=pd.merge(df1,df2,on='m',how='outer')
    g=g.fillna('')
##    print(c)
    print(pu)
    print(g)
    g.to_csv(r'/home/az2/Downloads/python_66/a/a1_out_pandas.txt', index=None, sep=';', mode='w+')
    
    #######################################



b()
##print(df1)
