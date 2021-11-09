# This script will write n no of files into a directory.
# For ETL.

no_of_files=1000

def bb(p):
    import pandas as pd; from faker import Faker;fake=Faker('en_US')

    d1=[];d2=[];d3=[];d4=[];d5=[]
    for x in range(30):
        d1.append(fake.country())
        d2.append(fake.state())
        d3.append(fake.address())
        d4.append(fake.credit_card_provider())
##        d5.append(fake.text())
    df1=pd.DataFrame([d1,d2,d3,d4])
    df2=df1.T
##    df2.rename(columns={'0': "a", '1': "c", '2': "nnn",'3': "dd"})
    df2.set_axis(['Country','State','Address','Credit_Card_Provider'],axis=1,inplace=True)
    print(df2.head(4))
    
    df2.to_csv('/home/az2/Downloads/bb33/cbb__' + str(p) + '.csv')
##    print(df2.columns)
##    data=pd.read_csv('/home/az2/Downloads/bb33/cbb__' + str(p) + '.csv')
##    print('cbb__' + str(p),'  ',data.columns)
    
    

for x in range(no_of_files):
    bb(x)


