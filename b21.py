import cx_Oracle

#print(cx_Oracle.clientversion())

#connection = cx_Oracle.connect("az2/1@192.168.1.70/1521")
connection = cx_Oracle.connect("az2/1@192.168.1.70/karachi2")


print (connection.version)
connection.close()



#conn = cx_Oracle.connect("az2", "1", "192.168.1.70/karachi2")


print("hlllllllll")
print("hello world")
