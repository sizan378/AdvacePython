# Nested Class

class Army:                     # Outer Class
    def __init__(self):
        self.name = 'Sizan'
        self.gn = self.Gun()    # Creatin Inner Class

    def show(self):
        print("Name:",self.name)

    class Gun:
        def __init__(self):
            self.name = 'AK47'
            self.capacity = '75 Round'
            self.length = '34.3 IN'
        def disp(self):
            print("Gun Name:", self.name)
            print("Catacity:", self.capacity)
            print("Length:", self.length)

a = Army()
a.show()
print(a.name)

print(a.gn.name)
a.gn.disp()
