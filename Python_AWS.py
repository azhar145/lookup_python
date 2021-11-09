import os

##os.system('python3 Pandas_Cloud9_Build_Enviornment.py')



##f=os.system('aws cloud9 list-environments')
####os.system('python3 Pandas_Delete_Cloud9_Enviornment.py')
##now = f.read()
####print ("Today is ", now)
##print(now)
##print("tt run")





import os
f = os.popen('ls -l')
now = f.read()
##print ("Today is ", now)
print(now)
