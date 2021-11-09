import json
import os
  
# Opening JSON file
u='uy'
os.system('aws cloud9 list-environments > ' + '/home/az2/Downloads/' + u +'.json')

f = open('/home/az2/Downloads/'+ u + '.json') 
  
data = json.load(f) 
  
k=1
for i in data['environmentIds']:
    
##    print("aws cloud9 delete-environment --environment-id ",i) 
##    print("kkkkk")
##    print("aws cloud9 delete-environment --environment-id ")
    os.system('aws cloud9 delete-environment --environment-id ' + i)
    print('\n', k,") aws cloud9 environment-id", i ," is going to be deleted in few mins ",i)
    k=k+1  
# Closing file 
f.close()

