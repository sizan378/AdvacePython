import mysql.connector

conn = mysql.connector.connect(user='sizan',password='1234', database='pdb',host='localhost',port=3306)

print('Befor ',conn.is_connected())

# Create Database Table

sql = 'INSERT INTO student(name, roll, fees) VALUES("ALam", 25416, 54.24),("Rahul", 854, 364.24),("Duck", 2544, 3954.24),("Karshof", 2784, 3636.24)'
myc = conn.cursor()
try:
    myc.execute(sql)
    conn.commit()
    print(myc.rowcount,"Row Inserted")
except:
    conn.rollback()
    print("Unable to Iserted Data")
myc.close()

conn.close()
print('After',conn.is_connected())
