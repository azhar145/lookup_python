import os
import pandas as pd
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 290)





def m(fa):
            
    f=open('/home/az2/Downloads/Medical/input/' + fa, 'r', encoding='ISO-8859-1')
   


    df1=pd.DataFrame(columns=['col_1','col_2','col_3','col_4'])
    df2=pd.DataFrame()
    for x in f:
##        print('xxxxxxxxxxxxxxxxxxxxxxx\n')
        p=x.split('|')
    ####    g=x.split('\n')
##        if p[0]=='PID':
##            print("")
##            print(p[0],'  ', str(f))

    ####    print(p[0])
    ####    print('\n')
    ##    print('Total lenght of record above is: ',len(p),'   ','  Last index is: ', p[len(p)-1])
    ####    print(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7])
        
    ##    print('\n')
    ##    print('<<<<<<<<<<<< record details with index (k is index) >>>>>>>>> \n')
        k=0
        while (k <= (len(p)-1)):
            
            if len(p[k]) > 0:
##                print('k=',k, '   ',p[k])
                df1=df1.append({'col_1':p[0],'col_2': k,'col_3': p[k],'col_4': fa},ignore_index=True)
##                print(df1)
##                mm(df1)
            k=k+1
##    print(df1)
    df2=df1.append(df1)
##    print(df2)
    return(df2)
##    mm(df1)                           
        
    ##    print('xxxxxxxxxxxxxxxxxxxxxxxx\n')
    ##    print('\n')
    ####    print(g[3])
    ##    print (p[0],p[1],p[2])

            
##    df2=df1.T
##    print(df2)

    
    ##print(df1.iloc[:6,[0,1]])



dfb=[]
for f in os.listdir('/home/az2/Downloads/Medical/input/'):
    # read file names in directory
    print(f)
##    m(f)
    hh=m(f)
    dfb=hh.append(hh)

print(dfb)
##dfc=dfb.T
##print(dfb)
##    print(hh)
##    print (m(f).df2)
##    x=dfb.append(m(f)
##print(dfb)    
##    s=mm()
##    print(s.df1)
##    dfb=df1.append(df1)
##    print(dfb)
##    mm(df1)

##print("output goes to: " +  '/home/az2/Downloads/dss45.txt')       


