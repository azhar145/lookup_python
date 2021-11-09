import pandas as pd;from faker import Faker
fake=Faker()
pd.set_option('display.max_rows', 90000)
pd.set_option('display.max_columns', 9000)
d1=[];d2=[];d3=[]

for x in range(500):
    d1.append(fake.zipcode_in_state())
    d2.append(fake.ipv4_public())
    d3.append(fake.country())

p=pd.DataFrame([d1,d2,d3])



p=p.T
p.set_axis(['color_name','ipv4_public','country'],axis=1,inplace=True)

##print(p.head(3))
##p.reset_index(drop=True)
##p.set_index(['h','j','pp'],inplace=True)
print(p.head(3))

n=p.pivot(index='color_name', columns='ipv4_public')['country']
print(n)



##print(p.pp.unique())
##print (p.groupby(['h']).size().sort())
##print(df1.groupby('ENODEB').sum())

##print(p['h'].value_counts())
##print(p.groupby(['h']).groups.keys())
##print(p.groupby(['h']).size())
##print(p.h.unique())
##print(df1.filter(like='_7', axis=0)
##
##print(p)
##
##n=p.pivot(index='j', columns='h')['pp']
##print(n)
##
##n1=p.pivot(index='j', columns='pp')['h']
##print(n1)
