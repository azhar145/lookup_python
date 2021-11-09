##import os
##os.system('ls')

import os
f = os.popen('ls -ltr')
now = f.read()
##print ("Today is ", now)
print(now)
