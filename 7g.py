def m(k):
    
    import pandas as pd; import os
    from faker import Faker
    fake=Faker()

    f=os.listdir('/home/az2/Downloads/bb33/')

    d1=[];d2=[]
    for x in  range(33):
        d1.append(fake.state())
        d2.append(fake.city())

    p=pd.DataFrame([d1,d2])
    p.to_csv('/home/az2/Downloads/bb33/' + 't77_' + str(k) + '.csv')


for k1 in range(33):
    m(k1)
    
