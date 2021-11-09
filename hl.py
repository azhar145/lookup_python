import subprocess

cmd = 'hdfs dfs -ls /user/path'.split() # cmd must be an array of arguments
files = subprocess.check_output(cmd).strip().split('\n')
for path in files:
  print (path)
