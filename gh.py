import os;import pandas as pd
from faker import Faker
fake=Faker()

d1=[];d2=[];d3=[]
##
for x in range(340):
    d1.append(fake.name())
    d2.append(fake.state())
    d3.append(fake.job())
##
    df=pd.DataFrame([d1,d2,d3])
####
df1=df.T

##print(df.head())
print(df1.iloc[[2,4,33],[0,1]])
print(df1.shape,'  ',df1.size)
