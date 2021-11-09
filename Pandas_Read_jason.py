import json 
  
# Opening JSON file 
f = open('/home/az2/Downloads/p76.json',) 
  
# returns JSON object as  
# a dictionary 
data = json.load(f) 
  
# Iterating through the json 
# list 
for i in data['environmentIds']: 
    print("aws cloud9 delete-environment --environment-id ",i) 
  
# Closing file 
f.close() 
