import sys
import subprocess
import pandas as pd

cmd = 'ls'
a = subprocess.Popen(cmd, stdout=subprocess.PIPE)
print(a)
##if sys.version_info[0] < 3: 
##    from StringIO import StringIO
##else:
##    from io import StringIO
##
##b = StringIO(a.communicate()[0].decode('utf-8'))
##
##df = pd.read_csv(b, sep=" ")

