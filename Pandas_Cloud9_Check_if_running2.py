import json 
import os

##p='poinbt'
####os.system('aws cloud9 create-environment-ec2 --name ' +  p + ' --description "created by azhar" --instance-type t2.micro --automatic-stop-time-minutes 30')
##
##g='aws cloud9 create-environment-ec2 --name ' +  p + ' --description "created by azhar" --instance-type t2.micro --automatic-stop-time-minutes 30'
##f = os.popen(g)
##now = f.read()
####print ("Today is ", now)
##print(now)



g='aws cloud9 list-environments'
f = os.popen(g)
now = f.read()
##print ("Today is ", now)
print(now)
