import os; import pandas as pd


df=pd.DataFrame()
p=os.listdir('/home/az2/Downloads/bd/')
for x in p:
    print(x)
    df=pd.read_csv('/home/az2/Downloads/bd/' + x)
##    df=pd.read_excel('/home/az2/Downloads/bd/' + x)
##    df1=df1.append(df)

##print(df)
    
    
