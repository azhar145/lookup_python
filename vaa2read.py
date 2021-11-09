import os
import pandas as pd

f=os.listdir('/home/az2/Downloads/bb33/')


df2=pd.DataFrame()
for x in f:
    df=pd.read_csv('/home/az2/Downloads/bb33/' + x)
##    print(x,df.count())
    
    df2=df2.append(df)
##    print(df2)
##    print(df2.count())
##    print('===========================================================')
##    print(df[['Country', 'State', 'Address', 'Credit_Card_Provider']])
##    t=g.append(x)
##    print(t.count)
##    t=g.append(c, ignore_index=True)
##    print(c)
##    print(x,' ---->      ', df.head())
##    print(x,' ---->  ', df.size)
##    print(x,' ---->  ',df.shape)
##    print(x,' ---->  ',df.info)
##    g.append(df[0],)
##    print(g)

##    ff=open('/home/az2/Downloads/bb33/' + x , 'r',  encoding='ISO-8859-1')
##    
##    for k in ff:
##        print(x,'   ',k)
##    ff.close()
print(df2.value_count())
    


