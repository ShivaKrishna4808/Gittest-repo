class Manager:
    def managerMethod(self):
        print("I am the Manager")

class employee_1(Manager):
    def emp_1method(self):
        print("I am the Employee 1")

class employee_2(Manager):
    def emp_2method(self):
        print("I am the Employee 2")

emp1 = employee_1()
emp2 = employee_2()

emp1.managerMethod()
emp1.emp_1method()

emp2.managerMethod()
emp2.emp_2method()



