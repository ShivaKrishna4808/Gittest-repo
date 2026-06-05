class student:
    stdcount = 0
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
        student.stdcount +=1

    @staticmethod
    def showcount():
        print(student.stdcount)
e1 = student("bhavana",25)
e2 = student("ravi",55)
e3 = student("sri",18)

print("Number of Student:")
student.showcount()
