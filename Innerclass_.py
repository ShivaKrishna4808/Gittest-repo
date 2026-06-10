class Orga:
    def __init__(self):
        self.inner1 = self.department1()
        self.inner2 = self.department2()

    def showName(self):
        print("Organization Name: tutorials Point")

    class department1:
        def displaydepartment1(self):
            print("In Department 1")

    class department2:
        def displaydepartment2(self):
            print("In department 2")

outer = Orga()
outer.showName()

inner1 = outer.inner1
inner1.displaydepartment1()
inner2 = outer.inner2
inner2.displaydepartment2()
