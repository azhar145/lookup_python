import os
import pandas as pd
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 290)



def m(fa):
    
    import pandas as pd

    g=[]
    g1=[]
    g11=[]
    dfc=[]

    f=open('/home/az2/Downloads/Medical/input/' + fa , 'r',  encoding='ISO-8859-1')
    f1=open('/home/az2/Downloads/Medical/output/u_out.txt', 'w+',  encoding='ISO-8859-1')
    for x in f:
        p=x.split('|')
        if (p[0]=='MSH' or p[0]=='PID' or p[0]=='EVN' or p[0]=='IN1' or p[0]=='IN2'):
    ##        print(p[0])
            k=0
            while (k <= (len(p)-1)):
     
                g.append(p[k])
                g1.append('col_' + str(k) + '_' + str(p[0]))
                f1.write(p[k])
                if k < (len(p)-1):
                    f1.write(',')
    ##            f1.write('*')
    ##            print(k)
                k=k+1
            print(p[0],' length is/no of elements are ',(len(p)-1))
        

    f.close()
    f1.close()

    ##f11=open('/home/az2/Downloads/Medical/output/u_out.txt', 'r',  encoding='ISO-8859-1')
    f1=open('/home/az2/Downloads/Medical/output/u_out2.txt', 'w+',  encoding='ISO-8859-1')
    k=0
    while (k <= (len(g1)-1)):
        f1.write(g1[k])
        f1.write(',')
        k=k+1
        if k == len(g1):
            f1.write('\n')
            f1.write('\n')
    f1.close()

    f1=open('/home/az2/Downloads/Medical/output/u_out2.txt', 'a',  encoding='ISO-8859-1')
    k=0
    while (k <= (len(g)-1)):
        f1.write(g[k])
        f1.write(',')
        k=k+1
        if k == len(g):
            f1.write('\n')
    f1.close()


    ##import pandas as pd
    pd.set_option('display.max_rows', 800)
    pd.set_option('display.max_columns', 590)
    ####pd.set_option('display.max_colwidth', 40)
    ##
    ##data = pd.read_csv('/home/az2/Downloads/Medical/output/u_out2.txt', sep=",",  encoding='ISO-8859-1')
    ##print (data)

    ##print(g)
    ##print(len(g))
    k=0

    print(len(g1))

    df = pd.DataFrame()
    df = pd.DataFrame(g,g1)
    df.to_csv('/home/az2/Downloads/Medical/output/u_out3.txt')

####
    ##print(df)
    dfbb=df.T
    print(dfbb)

##    dfc = pd.read_csv('/home/az2/Downloads/Medical/output/u_out3.txt')
##    dfb=dfc.append(dfc)
    ##print(df)
##    mm=['col_2_EVN','col_3_PID','col_7_PID','col_5_PID','col_10_PID','col_4_IN1']

    print('***********************************\n')


####
##    df.to_csv('/home/az2/Downloads/Medical/output/u_out3.txt')
####    dfb = pd.read_csv('/home/az2/Downloads/Medical/output/u_out3.txt',engine='python',usecols=['col_2_EVN','col_3_PID','col_7_PID','col_5_PID','col_10_PID','col_4_IN1'])
####
####
##    dfbb = pd.read_csv('/home/az2/Downloads/Medical/output/u_out3.txt',engine='python')
####


##    print(dfb)
    return(dfbb)
 

dfb=[]
for f in os.listdir('/home/az2/Downloads/Medical/input/'):
    # read file names in directory
    print(f)
##    m(f)
    hh=m(f)
    dfb=hh.append(hh)
    dfb.to_csv('/home/az2/Downloads/Medical/output/u_out4.txt')
    dfb = pd.read_csv('/home/az2/Downloads/Medical/output/u_out4.txt',engine='python',usecols=['col_2_EVN','col_3_PID','col_7_PID','col_5_PID','col_10_PID','col_4_IN1'])
####

print(dfb.columns)
print(dfb.head(4))


