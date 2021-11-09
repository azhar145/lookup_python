import json
import os
  
# Opening JSON file
u='pn9h'
os.system('aws cloud9 list-environments > ' + '/home/az2/Downloads/' + u +'.json')

f = open('/home/az2/Downloads/'+ u + '.json') 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list
##os.system('aws cloud9 list-environments')
for i in data['environmentIds']:
    print("aws cloud9 delete-environment --environment-id ",i) 
##    print("kkkkk")
##    print("aws cloud9 delete-environment --environment-id ")
    os.system('aws cloud9 delete-environment --environment-id ' + i)
    
##    print("aws cloud9 delete-environment --environment-id ",i) 
  
# Closing file 
f.close()
##os.system('aws cloud9 list-environments')
