class employee:
    def __init__(self,nm,sal):
        self.name = nm
        self.salary = sal

    def getName(self):
        return self.name
    def getSalary(self):
        return self.salary
    

class SalesOfficer(employee):
    def __init__(self,nm,sal,inc):
        super().__init__(nm,sal)
        self.incnt=inc
    def getSalary(self):
        return self.salary+self.incnt
    
e1 = employee("rajesh",90000)
print("Total salary for {} is Rs {}".format(e1.getName(),e1.getSalary()))
s1 = SalesOfficer("Kiran",10000,20000)
print("Total Salary for {} is Rs {}".format(s1.getName(),s1.getSalary()))
