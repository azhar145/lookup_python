import pandas as pd

g=[]
g1=[]
g11=[]

f=open('/home/az2/Downloads/Medical/input/u.txt', 'r',  encoding='ISO-8859-1')
f1=open('/home/az2/Downloads/Medical/output/u_out.txt', 'w+',  encoding='ISO-8859-1')
for x in f:
    p=x.split('|')
    if p[0]=='MSH':
##        print(p[0])
        k=0
        while (k <= (len(p)-1)):
 
            g.append(p[k])
            g1.append('col_' + str(k) + '_' + str(p[0]))
            f1.write(p[k])
            f1.write(',')
##            f1.write('*')
##            print(k)
            k=k+1
        print(p[0],' length is ',(len(p)-1))      

f.close()
f1.close()
##
f=open('/home/az2/Downloads/Medical/input/u.txt', 'r',  encoding='ISO-8859-1')
f1=open('/home/az2/Downloads/Medical/output/u_out.txt', 'a',  encoding='ISO-8859-1')
for x in f:
    p=x.split('|')
    if p[0]=='EVN':
##        print(p[0])
        k=0
        while (k <= (len(p)-1)):
            g.append(p[k])
            g1.append('col_' + str(k) +  '_' +  str(p[0]))
            f1.write(p[k])
            f1.write(',')
##            f1.write('*')
##            print(k)
            k=k+1
        print(p[0],' length is ',(len(p)-1))
g11.append(g)        
f.close()
f1.close()

f=open('/home/az2/Downloads/Medical/input/u.txt', 'r',  encoding='ISO-8859-1')
f1=open('/home/az2/Downloads/Medical/output/u_out.txt', 'a',  encoding='ISO-8859-1')
for x in f:
    p=x.split('|')
    if p[0]=='PID':
##        print(p[0])
        k=0
        while (k <= (len(p)-1)):
            g.append(p[k])
            g1.append('col_' + str(k)  + '_' +  str(p[0]))
            f1.write(p[k])
            f1.write(',')
##            f1.write('*')
##            print(k)
            k=k+1
        print(p[0],' length is ',(len(p)))      
g11.append(g)
f.close()
f1.close()

f=open('/home/az2/Downloads/Medical/input/u.txt', 'r',  encoding='ISO-8859-1')
f1=open('/home/az2/Downloads/Medical/output/u_out.txt', 'a',  encoding='ISO-8859-1')
for x in f:
    p=x.split('|')
    if p[0]=='IN1':
##        print(p[0])
        k=0
        while (k <= (len(p)-1)):
            g.append(p[k])
            g1.append('col_' + str(k)  + '_' +  str(p[0]))
            f1.write(p[k])
            f1.write(',')
##            f1.write('*')
##            print(k)
            k=k+1
        print(p[0],' length is ',(len(p)-1))      
g11.append(g)
f.close()
f1.close()

f=open('/home/az2/Downloads/Medical/input/u.txt', 'r',  encoding='ISO-8859-1')
f1=open('/home/az2/Downloads/Medical/output/u_out.txt', 'a',  encoding='ISO-8859-1')
for x in f:
    p=x.split('|')
    if p[0]=='IN2':
##        print(p[0])
        k=0
        while (k <= (len(p)-1)):
            g.append(p[k])
            g1.append('col_' + str(k)  + '_' +  str(p[0]))
            f1.write(p[k])
            f1.write(',')
##            f1.write('*')
##            print(k)
            k=k+1
        print(p[0],' length is ',(len(p)-1))
g11.append(g)
f.close()
f1.close()

f=open('/home/az2/Downloads/Medical/input/u.txt', 'r',  encoding='ISO-8859-1')
f1=open('/home/az2/Downloads/Medical/output/u_out.txt', 'a',  encoding='ISO-8859-1')
for x in f:
    p=x.split('|')
    if p[0]=='PV1':
##        print(p[0])
        k=0
        while (k <= (len(p)-1)):
            g.append(p[k])
            g1.append('col_' + str(k)  + '_' +  str(p[0]))
            f1.write(p[k])
            f1.write(',')
##            f1.write('*')
##            print(k)
            k=k+1
        print(p[0],' length is ',(len(p)-1))      
g11.append(g)
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


import pandas as pd
pd.set_option('display.max_rows', 800)
pd.set_option('display.max_columns', 590)
##pd.set_option('display.max_colwidth', 40)

##data = pd.read_csv('/home/az2/Downloads/Medical/output/u_out2.txt', sep=",",  encoding='ISO-8859-1')
##print (data)

##for x in g1:
##    print(x)
print(len(g11))
print(len(g1))

