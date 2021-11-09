def h(xa):
    import pandas as pd;from faker import Faker;fake=Faker('en_US')
    d1=[];d2=[];d3=[]
    for x in range(4):
        d1.append(fake.name())
        d2.append(fake.state())
        d3.append(fake.city())
        

    g=pd.DataFrame([d1,d2,d3])

    for x in range(4):
        g.append([d1,d2,d3])

    g=g.T
    print(g)
    g.to_csv('/home/az2/Downloads/bb33/fs__'+ str(xa) + '.csv')


    
    u=open('/home/az2/Downloads/bb33/fs__'+str(xa)+'.csv','a+')
    u.write('\n')
    u.write('\n')
    u.write('\n')
    u.write(str(xa))
    u.write('\n')
    u.write('jjjjjjjjjjjj')
           
##    print(x,'  ',"h(x)")
    u.close()



for x in range(4):
    print("call ------  ",x)
    h(x)
    print('\n')

    
