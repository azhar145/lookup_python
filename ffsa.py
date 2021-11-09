def m(k):
    
    import os; import pandas as pd
    from faker import Faker
    fake=Faker()

    df=pd.DataFrame()
    d1=[];d2=[];d3=[]
    for x in range (2900):
        d1.append(fake.state())
        d2.append(fake.city())
         
    df=pd.DataFrame([d1,d2])

    df1=df.T
    df1.set_axis(['ss','fs'], axis=1,inplace=True) 
    
    df1.to_csv('/home/az2/Downloads/bb33/' + '99a_' + str(k))
##    print(df1.ss.value_counts())
##    list_drop = ['fs']
##    df1.drop(list_drop, axis=1, inplace=True)
##    print(df1.loc[:,'ss'.duplicated()])
##    print(df1.loc[:,str('ss').duplicated()])
    print(df1.shape)
    df2=df1.loc[df1['fs'].duplicated(), :]
    print(df2.sort_values(by=['fs'],ascending=False))
    print(df2.shape)
##    print(df1.iloc[12:16,:])


x=1
m(x)
    
