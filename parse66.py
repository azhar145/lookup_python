f=open('/home/az2/Downloads/u1.txt')
##print(f.readlines())
##print('\n')
##print('\n')
##print('nnnnnnnnnnnnn*********************************\n')
for x in f:
    print('xxxxxxxxxxxxxxxxxxxxxxx\n')
    g=x.split('\n')
    print(g)
##    print('\n')
    p=x.split('|')
    print(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7])

    if p[0]=='IN1':
        print('***  ',p[11])
    

    
    print('xxxxxxxxxxxxxxxxxxxxxxxx\n')
    print('\n')

##print(f.read())
##print(f.read())
##for x in f:
##    p=x.split('|')
##    g=x.split('||')
##    print('*********************************\n')
####    print(p[0],g[0])
##    print(p[0],
