import os;import pandas as pd
from faker import Faker
fake=Faker()

g=os.listdir('/home/az2/Downloads/bb33/')

m=pd.DataFrame()
for x in g:
    p=pd.read_csv('/home/az2/Downloads/bb33/' + x)
    m=m.append(p)

    
print(m)


