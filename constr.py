class employee:
    'Common base class for all employees'
    def __init__(self):
        self.name = "Bhavana"
        self.age = 24

e1 = employee()
print("name:{}".format(e1.name))
print("age:{}".format(e1.age))