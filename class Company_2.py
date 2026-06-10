class Company:
    def company(self):
        print("ABC Technologies")

class Department(Company):
    def department(self):
        print("Data Engineering")

class TeamLead(Department):
    def lead(self):
        print("Team Lead")

class Employee(TeamLead, Company):
    def employee(self):
        print("Software Engineer")

emp = Employee()

emp.company()
emp.department()
emp.lead()
emp.employee()