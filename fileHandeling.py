# Create File 

f = open("student.txt", mode='w')
f.write('Hello')
f.write('How Are You')
f.close()
print('Write Success')

f = open('student.txt', mode = 'r')
data = f.read()
print(data)
f.close()

f = open('student.txt', mode='rb')
data = f.read()
print(data)
f.close()
