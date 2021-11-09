import os
import pandas as pd
##m=[]
##x = os.popen('ls -ltr > test53.txt','r')
##t=x.readline()
##c=open("test53.txt")
##g=pd.read_csv('/home/az2/Downloads/test53.txt', delimiter= '\t')

##data = pd.read_csv("/home/az2/Downloads/test53.txt", encoding="ISO-8859-1", sep='az2')
##print(data)

##print(open('/home/az2/Downloads/test53.txt').read())
##g = [(0, 8), (8, 20), (0, 33),(700,760)]
##g = [(0, 3), (3, None)]
##g = [ ‘infer’ ] index_col=1
##df = pd.read_fwf('/home/az2/Downloads/test53.txt', header=None,delim_whitespace=True)
df=pd.read_fwf('/home/az2/Downloads/test53.txt', colspecs='infer', widths=None, header=None)
##df = pd.read_csv('/home/az2/Downloads/test53.txt', header=None,delim_whitespace=True)


##df = pd.read_csv('/home/az2/Downloads/test53.txt', skiprows=range(9), header=None, delim_whitespace=True)

##print(df.shape)
print(df[[8,7,6,5]])
####m=c.read()
##for x in g:
####    x=c.readline
####    x=x.split()
####    b=x.split()
####    g=pd.Dataframe(b)
####    print(g.shape)
##
##    print(x)
##    
##    
##    
####p=m.split()
####print(p)
##g.close()




##
##df = pd.read_csv('test53.txt', delimiter='\t')
####df = pd.read_csv('test53.txt',  delimiter= '\s+')
####df=pd.read_csv('test53.txt', delimiter="\t", header=None)
##print(df.shape)



##print(t)
##df1=pd.DataFrame(t)
##print(df1)


##for x in t:
##    df=m.append(x)
##    df1=pd.DataFrame(df)


    
##    print(x.split())
##df=m.append(t)
##df1=pd.DataFrame(df)
##print(df1.head())
##print(t)



##fox x in t:
##    m.append(x)
    
##print ("This is the name of the script: ", sys.argv[0])
##print ("Number of arguments: ", len(sys.argv))
##print ("The arguments are: " , str(sys.argv))




##import time,sys
##import subprocess
##import os,pandas
##from datetime import datetime
###c=open("//home/az2/Downloads/u"_
##now = datetime.now()
##dt_string2 = now.strftime("%d/%m/%Y %H:%M:%S")
##dt_string = now.strftime("%m_%Y %H:%M:%S")
##print("date and time =", dt_string)
##c=open("//home/az2/Downloads/u" + dt_string +'.txt','w+')
##c.write('hello ')
##c.write(dt_string)
##c.close()
####s=os.system()
####output = s.readlines()
####print(s)
##
###o=os.popen('ls').read()
###print(o[0,5])
###command = os.popen2('ls -al')
###t=command.read().split()
###print(t[3])
###print(command.close())
##
####stream = os.popen('aws s3 ls')
####output = str(stream.readlines())
####print(output[[2,3]])
##
##stream = os.popen('ls -l')
##output = stream.read()
##
##with open(sys.argv[1], 'r') as f:
##    contents = f.read()
##
####data = []
######print(output.head())
####for x in pd.
####m=data.append(output)
####print(m)
