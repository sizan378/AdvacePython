import mysql.connector

conn = mysql.connector.connect(user='sizan',password='1234',host='localhost',port=3306)

print('Befor ',conn.is_connected())

# Create Database Using Cursor

# sql = "SHOW DATABASES "
sql = " CREATE DATABASE pdb"
myc = conn.cursor()
myc.execute(sql)
# for d in myc:
#     print(d)
myc.close()

conn.close()
print('After',conn.is_connected())
