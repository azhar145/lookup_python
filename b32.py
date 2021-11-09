import cx_Oracle
import os
import sys

print(sys.version)
print(os.environ['ORACLE_HOME'])
#print(os.environ['path'])



con = cx_Oracle.connect("az2/1@192.168.1.70:1521/karachi2")

#con = cx_Oracle.connect('USER/pass@host:port/SID')
print (con.version)

con.close()
