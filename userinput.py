import mysql.connector

conn = mysql.connector.connect(user='sizan',password='1234', database='pdb',host='localhost',port=3306)

print('Befor ',conn.is_connected())

# Create Database Table

sql = 'INSERT INTO student(name, roll, fees) VALUES(%s, %s, %s)'
myc = conn.cursor()
nm = input('Enter Your Name:')
ro = int(input('Enter Roll:'))
fe = float(input('Enter Fees:'))
params = (nm,ro,fe)
try:
    myc.execute(sql, params)
    conn.commit()
except:
    conn.rollback()
myc.close()

conn.close()
print('After',conn.is_connected())
