##import os
##from os.path import abspath, realpath
##
##
##os.chdir('/usr/lib/oracle/xe/app/oracle/product/10.2.0/server/network/admin')
##
##p1='liborasdkbase.so'
##
##print(p1,'   ',abspath(p1), '  ',realpath(p1))


import cx_Oracle
##import db_config

##con = cx_Oracle.connect(db_config.user, db_config.pw, db_config.dsn)
##
##print(cx_Oracle.version)

con = cx_Oracle.connect('Azhar2/abcd@192.168.1.70')
print(con.read())
