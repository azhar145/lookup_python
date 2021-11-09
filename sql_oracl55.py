"""
ATTENTION:
When using executemany with a list of tuples, the numbers representing the rows has to be strictly from 1 to the last. Or else it won't work.
I really don't understand why.
"""

import cx_Oracle
from parserFWF import getConfigDF

HOTEL_CONFIG = getConfigDF() #dataframe

create_table = '''CREATE TABLE HOTEL_DIMENSION (
                        OID NUMBER(38,0) NOT NULL, 
                        PROPERTY_ID VARCHAR2(8),
                        HOTEL_NAME NVARCHAR2(64),
                        CITY_CODE VARCHAR2(4),
                        CITY_NAME VARCHAR2(64),
                        COUNTRY_NAME VARCHAR2(64),
                        CHAIN_CODE VARCHAR2(4),
                        CHAIN_NAME VARCHAR2(64),
                        "LOCK" VARCHAR2(4),                       
                        ADDR NVARCHAR2(255),
                        MADE_ON TIMESTAMP
                        )''' 
con = cx_Oracle.connect('system','1',cx_Oracle.makedsn('192.168.1.70','1521','XE'))
cur = con.cursor()
cur.execute('DROP TABLE HOTEL_DIMENSION')
cur.execute(create_table)

rows = [tuple(x) for x in HOTEL_CONFIG.values]
cur.executemany('''INSERT INTO HOTEL_DIMENSION (PROPERTY_ID,OID,
                                         HOTEL_NAME,CITY_CODE,CITY_NAME,
                                         COUNTRY_NAME,CHAIN_CODE, CHAIN_NAME,"LOCK",
                                         ADDR,MADE_ON) 
                                         VALUES (:2,:1,:3,:4,:5,:6,:7,:8,:9,:10,:11)''',rows)
con.commit()

cur2 = con.cursor()
cur2.execute("SELECT * FROM HOTEL_DIMENSION")
print (cur2.fetchall())

cur.close()
cur2.close()
