def tt(m):
    import pandas as pd;from faker import Faker;import glob
    fake=Faker()
    for f in glob.glob('/home/az2/Downloads/bb33/*.csv'):
        os.remove(f)

    d1=[];d2=[];d3=[]

    for x in range(3):
        d1.append(fake.state())
        d2.append(fake.city())
        d3.append(fake.age())

    p=pd.DataFrame([d1,d2,d3])
    p=p.T
    print(p)
    p.to_csv('/home/az2/Downloads/bb33/ggr_' + str(m) + '.csv')



##for m in range(33):
##    import os
##    os.remove('/home/az2/Downloads/bb33/*.csv')
##    tt(m)
