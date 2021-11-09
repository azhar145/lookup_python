import os
import pandas as pd
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 590)
pd.set_option('display.max_colwidth', 40)

def m(fa):
            
    f=open('/home/az2/Downloads/Medical/input/' + fa, 'r')
   
    print(fa)

    df1=pd.DataFrame(columns=['col_1','col_2','col_3','col_4','col_5','col_6'])
    df2=pd.DataFrame()
    for x in f:
##        print('xxxxxxxxxxxxxxxxxxxxxxx\n')
        p=x.split('|')

    ##    print('<<<<<<<<<<<< record details with index (k is index) >>>>>>>>> \n')
        k=0
        while (k <= (len(p)-1)):
            
            if len(p[k]) > 0:
                df1=df1.append({'col_1':p[0],'col_2': k,'col_3': p[k],'col_4': fa,'col_5': (str(p[0]) + str(k)), 'col_6': p[0]},ignore_index=True)
##                print(df1)

            k=k+1

    df2=df1.append(df1)

    return(df2)
    f.close()


            
##    df2=df1.T
##    print(df2)

dfb=pd.DataFrame()

for f in os.listdir('/home/az2/Downloads/Medical/input/'):
    # read file names in directory
##    print(f)
##    m(f)
    hh=m(f)
    print(f,' printed  ',hh)
##    dfb=hh.append(hh)
    dfb=dfb.append(hh)
    

print(dfb)
##    print(hh)

##print(dfb)
##dfc=dfb.T
##print(dfb)


##print("output goes to: " +  '/home/az2/Downloads/dss45.txt')       


