class Employee:
    def __init__(self,name,age,salary):
        self.name = name
        self._age= age
        self._salary = salary

    def displayEmployee(self):
        print("Nmae: ",self.name,",age: ",self._age,",salary: ",self._salary)

e1 = Employee("Bhavana",24,10000)

print(e1.name)
print(e1._age)
print(e1._salary)