##import os  
##path = 'C:/Temp/cx2/*'   
##p=os.listdir('C:/Temp/cx2/')
##
##m=open(x,'r')
##print(m)

##for x in p:
##    print(x)
##    m=open(x,'r')
##    m.close()
##    f=open(file, 'r')  
##    print (f.file,'\n')   
##    f.close()


import glob   
path = 'C:/Temp/cx/*'   
files=glob.glob(path)   
for file in files:     
    f=open(file, 'r')  
    print(f.readlines())   
    f.close() 
