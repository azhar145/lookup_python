import pandas as pd
import os


##df2=pd.DataFrame(columns=['m','pb','h'])

##print(df1)
##print(df2)

d1=[];d2=[];d3=[]

for c in range(33):
    d1.append(c)
    d2.append(c+65)
    d3.append(c/4)

df1=pd.DataFrame([d1,d2,d3])
df1=df1.T
df1.set_axis(['Hy','jy','hh'],axis=1,inplace=True)
print(df1)                 
