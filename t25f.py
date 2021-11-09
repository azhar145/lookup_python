import os; import os.path; import pandas as pd
from faker import Faker;from pathlib import Path
fake=Faker()


m=os.path.isdir('/home/az2/Downloads/t42')
print(m)
if m == True:
    print("directory exist")
    os.rmdir('/home/az2/Downloads/t42')
else:
    print("directory doesnot exist")
##    os.path.mkdir('/home/az2/Downloads/t42')
    print('directry created')
##os.rmdir("/home/az2/Downloads/t42")

##g=os.listdir("home/az2/Downloads/t42")
##tt = os.path.isdir(m)
##print("llll",tt)
