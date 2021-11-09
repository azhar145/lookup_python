import os
import pandas as pd
m=[]
command = os.popen('ls -al','r')
t=command.read()
##print(t)
df1=pd.DataFrame(t)
print(df1)
##df1=pd.DataFrame(list(t.items()))
##df1 = pd.read_clipboard()
##for x in t:
##    df=m.append(x)
##    df1=pd.DataFrame(df)

##print(df1.head())
    
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
