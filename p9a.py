import os;import pandas as pd
from faker import Faker
fake=Faker()

d1=[];d2=[];d3=[]

m=pd.DataFrame()
for x in range(300):
    d1.append(fake.state())
    d2.append(fake.city())
    d3.append(fake.building_number() + fake.address())
    
    m=pd.DataFrame([d1,d2,d3])
m=m.T    
print(m)
