#import urllib.request
##import re
##import pandas as pd

def b():
    f1=open('/home/az2/Downloads/python_66/a/a1.txt','r')
    g=f1.readlines()

    m='azhar'
    n='idno'

##    pv=pd.DataFrame(columns=['m','pp'])

    k=0 
    for x in g:
        k=k+1
        if ((n in x) or (m in x)):
            
            t1=x.index(m,0)
            t2=x.index(n,0)
            sa1=x[t1:t1+12]
            sa2=x[t2:t2+6]
            print(k,',',sa1,',',sa2)
##        if m in x:
##            t1=x.index(m,0)
##            sa=x[t1:t1+12]
##            print(k,',',sa)
##        if n in x:
##            t2=x.index(n,0)
##            sb=x[t2:t2+12]
##            print(k,',',sb.split())      
##         print(sa,sb)   

b()
