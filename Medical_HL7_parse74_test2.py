import os
import pandas as pd
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 590)
pd.set_option('display.max_colwidth', 40)

def m(fa):
            
    f=open('/home/az2/Downloads/Medical/input/' + fa, 'r',  encoding='ISO-8859-1' )

    df1=pd.DataFrame(columns=['col_1','col_2','col_3','col_4','col_5','col_6'])
    df_MSH=pd.DataFrame(columns=['MSH_col_1','MSH_col_2','MSH_col_3'])
    df_PID=pd.DataFrame(columns=['PID_col_1','PID_col_2','PID_col_3'])
                        
    for x in f:
        p=x.split('|')
        if (p[0]=='MSH'):           
##            print(fa,' ---> ',len(p)-1,'   ',p)           
            k=0
            while (k <= (len(p)-1)):
                if len(p[k]) > 0:
##                    pass
                    df_MSH=df_MSH.append({'MSH_col_1':k,'MSH_col_2': p[0],'MSH_col_3': p[1]},ignore_index=True)
    ##                print(df1)
##                    df2=df2.append(p)
                k=k+1
        elif (p[0]=='PID'):
##            print(fa,' ---> ',len(p)-1,'   ',p) 
##            print(fa,' ---> ',p)           
            k=0
            while (k <= (len(p)-1)):
    ##            print (p)
                if len(p[k]) > 0:
##                    pass
                    df_PID=df_PID.append({'PID_col_1':fa,'PID_col_2': k,'PID_col_3': p[0]},ignore_index=True)
##                    df1=df1.append({'col_1':p[0],'col_2': k,'col_3': p[k],'col_4': fa,'col_5': (str(p[0]) + str(k)), 'col_6': p[0]},ignore_index=True)

                k=k+1
        elif (p[0]=='EVN'):
##            print(fa,' ---> ',len(p)-1,'   ',p) 
    ##            print(fa,' ---> ',p)           
            k=0
            while (k <= (len(p)-1)):
    ##            print (p)
                if len(p[k]) > 0:
    ##                    pass
                    
                    df1=df1.append({'col_1':p[0],'col_2': k,'col_3': p[k],'col_4': fa,'col_5': (str(p[0]) + str(k)), 'col_6': p[0]},ignore_index=True)

                k=k+1             
          

    f.close()
    return (df_MSH)


 
    

dfb=pd.DataFrame()

for f in os.listdir('/home/az2/Downloads/Medical/input/'):

##    m(f)
    hh=m(f)
    print(f,' printed  ')
##    print(f,' printed  ',hh)
##    dfb=hh.append(hh)
    dfb=dfb.append(hh)
    print(dfb)
    print('**********************************')
      


