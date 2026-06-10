class a:
    def show(self):
        print("Class A")

class b(a):
    def show(self):
        print("Class B")
        super().show()

class c(a):
    def show(self):
        print("Class C")
        super().show()
    

class d(b,c):
    def show(self):
        print("Class D")
        super().show()

D=d()
D.show()
