import mysql.connector

conn = mysql.connector.connect(user='sizan',password='1234', database='pdb',host='localhost',port=3306)

print('Befor ',conn.is_connected())

# Create Database Table

sql = 'CREATE TABLE student1(id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), roll INT, fees FLOAT)'
myc = conn.cursor()
myc.execute(sql)
myc.close()

conn.close()
print('After',conn.is_connected())
