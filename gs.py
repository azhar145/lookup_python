def n(k):
    import os; import pandas as pd
    from faker import Faker
    fake=Faker()

    ##b=os.listdir('/home/az2/Downloads/bb3')


    d1=[];d2=[]
    df=pd.DataFrame()
    for x in range(10):
        d1.append(fake.state())
        d2.append(fake.city())
        df=pd.DataFrame([d1,d2])

    df1=df.T

    print(df1)    
    df1.to_csv('/home/az2/Downloads/bb33/' + 'aaa_'+ str(k)) 

import os
b=os.listdir('/home/az2/Downloads/bb33')
for x in range(25):
    n(x)
    
