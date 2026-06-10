class student:
    def __init__(self,name="shiva",marks=53):
        self.name= name
        self.marks = marks

s1 = student()
s2 = student("Krishna",54)

print(f"Name: {s1.name} marks: {s1.marks}") 
print(f"name is {s2.name} and marks are {s2.marks}")


# class Student:
#    def __init__(self, name="Rajaram", marks=50):
#       self.name = name
#       self.marks = marks

# s1 = Student()
# s2 = Student("Bharat", 25)

# print ("Name: {} marks: {}".format(s1.name, s2.marks))
# print ("Name: {} marks: {}".format(s2.name, s2.marks))