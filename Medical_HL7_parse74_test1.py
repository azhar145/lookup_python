import os
import pandas as pd
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 590)
pd.set_option('display.max_colwidth', 40)

def m(fa):
            
    f=open('/home/az2/Downloads/Medical/input/' + fa, 'r',encoding='latin-1')

##
    df1=pd.DataFrame(columns=['col_1','col_2','col_3','col_4','col_5','col_6'])
##    df2=pd.DataFrame()
    for x in f:
        p=x.split('|')
        if (p[0]=='MSH'):           
            print(fa,' ---> ',len(p)-1,'   ',p)           
            k=0
            while (k <= (len(p)-1)):
                
    ##            print (p)
                if len(p[k]) > 0:
                    
##                    pass
                    
                    
                    df1=df1.append({'col_1':p[0],'col_2': k,'col_3': p[k],'col_4': fa,'col_5': (str(p[0]) + str(k)), 'col_6': p[0]},ignore_index=True)
    ##                print(df1)
##                    df2=df2.append(p)
                k=k+1
        elif (p[0]=='PID'):
            print(fa,' ---> ',len(p)-1,'   ',p) 
##            print(fa,' ---> ',p)           
            k=0
            while (k <= (len(p)-1)):
    ##            print (p)
                if len(p[k]) > 0:
##                    pass
                    
                    df1=df1.append({'col_1':p[0],'col_2': k,'col_3': p[k],'col_4': fa,'col_5': (str(p[0]) + str(k)), 'col_6': p[0]},ignore_index=True)
    ##                print(df1)
##                    df2=df2.append(p)
                k=k+1       
          
##    df2=df1.append(df1)
##    df2=df1.T
##    print(df2[0],df2)
##    return(df2)
    f.close()


 
    

dfb=pd.DataFrame()

for f in os.listdir('/home/az2/Downloads/Medical/input/'):

    m(f)
##    hh=m(f)
##    print(f,' printed  ')
##    print(f,' printed  ',hh)
##    dfb=hh.append(hh)
##    dfb=dfb.append(hh)
    
##
####print(dfb)
##print(dfb.columns)
##print(dfb.index)
##print(dfb.shape)
##print(dfb.head(4))
##dfb['new_col']=dfb['col_5']+'_'+dfb['col_4']
##print(dfb.head(4))
####    print(hh)
##dfb.reset_index(drop=True)
##dfb.set_index('new_col',inplace=True)
##print(dfb)
##
####print(dfb)
####dfc=dfb.T
####print(dfb)
##
##
####print("output goes to: " +  '/home/az2/Downloads/dss45.txt')       


