# Passing Member of one Class to Another Class

class Student:
    # Constructor
    def __init__(self, n, r):
        self.name = n
        self.roll = r

    # Instance Method
    def disp(self):
        print("Student Name:", self.name)
        print("Student Roll:", self.roll)

class User:
    #Statice Method
    @staticmethod
    def show(s):
        print("User name:",s.name)
        print("User Roll:", s.roll)
        s.disp()

# Create Object of student Class
stu = Student('sizan',1703)

User.show(stu)