class employee:
    "Common base class for all employees"
    def __init__(self,name,age):
        self.name = name
        self.age = age

e1 = employee("Bhavana",24)
e2 = employee("Bharat",25)

print("name:{}".format(e1.name))
print("age:{}".format(e1.age))
print("name:{}".format(e2.name))
print("age:{}".format(e2.age))