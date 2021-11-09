def n(t):

    import os;import pandas as pd
    from faker import Faker

    fake=Faker()

    p=os.listdir('/home/az2/Downloads/')

    d1=[];d2=[]
    df=pd.DataFrame()
    for x in range(40):
        d1.append(fake.state())
        d2.append(fake.city())
        df=df.append(d1,d2)
        
    print(df)
    df.to_csv('/home/az2/Downloads/bd/' + '__' + str(t))

import os
##os.rmdir('/home/az2/Downloads/bd/*')
##os.mkdir('/home/az2/Downloads/bd/gg2/')
p=os.listdir('/home/az2/Downloads/bd/')
for x in p:
    print(os.remove(os.path.join(p,x)))
    
##    n(x)
##    
