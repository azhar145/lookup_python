import os
import pandas as pd
##m=[]
##x = os.popen('ls -ltr > test53.txt','r')
##t=x.readline()
c=open("test53.txt")
##df=pd.DataFrame(c.split())
##print(df)
####m=c.read()
##for x in c:
##    x=c.readline
##    x=x.split()
####    b=x.split()
####    g=pd.Dataframe(b)
####    print(g.shape)
####    g=pd.Dataframe(x.split())
##    print(x)
##
##d=c.split()
d=c.readlines()
print(d)
##for x in d:
##    print(x)
##    df=pd.DataFrame(x)
####    print(x.split(),sep='---',end='\n')
####    print("=========")
##    print(df.head(2))
