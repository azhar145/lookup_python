def a():
    import re
##    print("j")

    f=open("/home/aa/Downloads/g/qoffset_freq_change_3.txt",'r')
    g=open("/home/aa/Downloads/qoffset_freq_before_tabular.txt",'r')

    f2=open("/home/aa/Downloads/g/qoffset_freq_change_3mmmmmm.txt",'w+')
    g2=open("/home/aa/Downloads/qoffset_freq_before_tabularnnnnnnn.txt",'w+')
    for x in f:
##        m=x.strip("-")
##        print(x.split('EUtranCellFDD=')[1],' ========')
##        print(x.split('EUtranCellFDD=')[1].split(',')[0] ,'  ',x.split('EUtranCellFDD=')[1].split(',')[1])
        f2.write(x.split('EUtranCellFDD=')[1].split(',')[0] + '      ' + x.split('EUtranCellFDD=')[1].split(',')[1])
        f2.write("\n")
        
##    print("/n")
##    print('---------------------')


    for x1 in g:
##        m=x.strip("-")
##        print(x.split('EUtranCellFDD=')[1],' ========')
##        m=x.split()
##        print(m[1:])
        g2.write(str(x1.split())
        g2.write("\n")
        
##        print(x.split('EUtranCellFDD=')[1].split(',')[0] ,'  ',x.split('EUtranCellFDD=')[1].split(',')[1])
##        f2.write(x.split('EUtranCellFDD=')[1].split(',')[0] + '      ' + x.split('EUtranCellFDD=')[1].split(',')[1])
##        f2.write("\n")
        
##    print("/n")
##    print('---------------------')        


a()    
