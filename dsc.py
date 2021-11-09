import pandas as pd;import os

g=os.listdir('/home/az2/Downloads/bb33/')

k=0
df2=pd.DataFrame()
for x in g:
    df=pd.read_csv('/home/az2/Downloads/bb33/' + x)
##    df=df.head(1)
    df2=df2.append(df)
    k=k+1
##df3=df2.T

pd.set_option("display.max_rows",80)
pd.set_option("display.max_columns",380)    

##pd.display_values    
print(df2)
print(k,'    ',df2.shape,'  ',df2.size)

