class Employee:
    'Common base class for all employees'
    def __inti__(self,name='Bhavana',age=24):
        self.name = name
        self.age = age

e1 = Employee()

# e2 = Employee('Bharat','26')

print("name: {}".format(e1.name))
print("age: {}".format(e1.age))
# print('name: {}'.format(e2.name))
# print("age: {}".format(e2.age))

# class Employee:
#    'Common base class for all employees'
#    def __init__(self, name="Bhavana", age=24):
#       self.name = name
#       self.age = age

# e1 = Employee()
# e2 = Employee("Bharat", 25)

# print ("Name: {}".format(e1.name))
# print ("age: {}".format(e1.age))
# print ("Name: {}".format(e2.name))
# print ("age: {}".format(e2.age))