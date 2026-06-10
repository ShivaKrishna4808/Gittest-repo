class Employee:
    def __init__(self,name='Bhavana',age = 25):
        self.name = name
        self.age= age

e1 = Employee()
e2 = Employee('Bharat',32)

print("Name:{}".format(e1.name))
print("age:{}".format(e1.age))
print("name:{}".format(e2.name))
print("age:{}".format(e2.age))