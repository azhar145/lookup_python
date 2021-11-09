import cx_Oracle
print(cx_Oracle.version)

ip = '192.168.1.70'
port = 1521
SID = 'orcl'
dsn_tns = cx_Oracle.makedsn(ip, port, SID)
db = cx_Oracle.connect('Azhar2', 'abcd', dsn_tns)
##c = db.cursor()
