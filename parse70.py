import pandas as pd
f=open('/home/az2/Downloads/u1.txt')
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 90)


df1=pd.DataFrame(columns=['col_1','col_2'])

for x in f:
    print('xxxxxxxxxxxxxxxxxxxxxxx\n')
    p=x.split('|')
####    g=x.split('\n')
    if p[0]=='PID':
        print(p[0])

####    print(p[0])
####    print('\n')
##    print('Total lenght of record above is: ',len(p),'   ','  Last index is: ', p[len(p)-1])
####    print(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7])
    
##    print('\n')
##    print('<<<<<<<<<<<< record details with index (k is index) >>>>>>>>> \n')
    k=0
    while (k <= (len(p)-1)):
        
        if len(p[k]) > 0:
            print('k=',k, '   ',p[k])
            df1=df1.append({'col_1':p[0],'col_2': p[k]},ignore_index=True)
        k=k+1
                           
    
##    print('xxxxxxxxxxxxxxxxxxxxxxxx\n')
##    print('\n')
####    print(g[3])
##    print (p[0],p[1],p[2])
df2=df1.T
print(df2)
##print(df1.iloc[:6,[0,1]])


    


