##MSH|^~\&|ADT1|MCM|LABADT|MCM|198808181126|SECURITY|ADT^A01|MSG00001-|P|2.6
##EVN|A01|198808181123
##PID|||PATID1234^5^M11^^AN||stupid azhar||19610615|M||2106-3|677 DELAWARE AVENUE^^EVERETT^MA^02149|GL|(919)379-1212|(919)271-3434~(919)277-3114||S||PATID12345001^2^M10^^ACSN|123456789|9-87654^NC
##NK1|1|JONES^BARBARA^K|SPO|||||20011105
##NK1|1|JONES^MICHAEL^A|FTH
##PV1|1|I|2000^2012^01||||004777^LEBAUER^SIDNEY^J.|||SUR||-||ADM|A0
##AL1|1||^PENICILLIN||CODE16~CODE17~CODE18
##AL1|2||^CAT DANDER||CODE257
##DG1|001|I9|1550|MAL NEO LIVER, PRIMARY|19880501103005|F
##PR1|2234|M11|111^CODE151|COMMON PROCEDURES|198809081123
##ROL|45^RECORDER^ROLE MASTER LIST|AD|RO|KATE^SMITH^ELLEN|199505011201
##GT1|1122|1519|BILL^GATES^A
##IN1|001|A357|1234|BCMD|||||132987
##IN2|ID1551001|123456789
from faker import Faker
fake = Faker('en_US')
xx=fake.first_name_female()+' ' +fake.last_name()
f=open('/home/az2/Downloads/Medical/input/u.txt'  , 'r',  encoding='ISO-8859-1')
##    f1=open('/home/az2/Downloads/Medical/output/u_out.txt', 'w+',  encoding='ISO-8859-1')
##    print(f)

##wds = ["red", "blue", "green"]
##glue = ';'
##s = glue.join(wds)
##print(s)
##print(wds)


g=open('/home/az2/Downloads/Medical/input/u77.txt'  , 'w+',  encoding='ISO-8859-1')
##g=open('/home/az2/Downloads/Medical/input/u77.txt'  , 'w+',  encoding='ISO-8859-1')

for x in f:

    print('\n\***************  original ***********\n\n  ',x)
##    print(len(x))

    
    pa=x.split('\n')
    print('\n\nsplit by each line\n\n',pa)
    print(pa)
##    print(len(pa))
    
    pb=x.split('|')
    print('\n\nsplit with pipe\n\n ',pb)
##    print(len(pb))

    print('\n\n********* join **********\n\n ',pb)
    glue = '|'
    s = glue.join(pb)
    print(s)
    
    print('\n****************\n')
##    p=pa.split('|')
##    g.write(p)
##    print(p)
##    print('\n')
##    g.write(pa)
##    p=x.split('|')
##    print(p)
##    g.write(str(p))
##    if (p[0]=='PID'):
##        print('\n')
##        k=0
##        while (k <= (len(p)-1)):
##            p[5]=xx
##            p[3]=xx
##            if p[3]==xx:
##                p[8]='F'
##    
##            p[7]=fake.msisdn()
##                
##            p[18]=xx
##            p[13]=fake.phone_number
##            p[11]=fake.address()
##            print(k,'   ',p[k])
##            k=k+1
g.close()           


##for x in f:
##    p=x.split('|')
####    print(p)
##    if (p[0]=='PID'):
##        k=0
##        while (k <= (len(p)-1)):
##            glue = '|'
##            s = glue.join(wds)
##            print(s)
##            k=k+1
##            
        

        
##            
##        
##            while (k <= (len(p)-1)):
##        if (p[0]=='MSH' or p[0]=='PID' or p[0]=='EVN' or p[0]=='IN1' or p[0]=='IN2'):
##    ##        print(p[0])
##            k=0
##            while (k <= (len(p)-1)):
####                print(p[k])
##                g.append(p[k])
##                g1.append('col_' + str(k) + '_' + str(p[0]))
####                f1.write(p[k])
####                if k < (len(p)-1):
####                    f1.write(',')
##                   
##    ##            f1.write('*')
##    ##            print(k)
##            k=k+1
##            print(fa,'  ',p[0],' length is/no of elements are ',(len(p)-1))
    


f.close()

