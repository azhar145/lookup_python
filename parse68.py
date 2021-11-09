f=open('/home/az2/Downloads/u1.txt')

for x in f:
    print('xxxxxxxxxxxxxxxxxxxxxxx\n')
    p=x.split('|')
##    g=x.split('\n')
    if p[0]=='PID':
        print(p[0])

##    print(p[0])
####    print('\n')
    print('Total lenght of record above is: ',len(p),'   ','  Last index is: ', p[len(p)-1])
####    print(p[0],p[1],p[2],p[3],p[4],p[5],p[6],p[7])
    
    print('\n')
    print('<<<<<<<<<<<< record details with index (k is index) >>>>>>>>> \n')
    k=0
    while (k <= (len(p)-1)):
        
        if len(p[k]) > 0:
            print('k=',k, '   ',p[k])
        k=k+1
                           
    
    print('xxxxxxxxxxxxxxxxxxxxxxxx\n')
    print('\n')
##    print(g[3])
    print (p[0],p[1],p[2])


