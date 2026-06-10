# Const using Instance methods "Loops"

class student:
    def __init__(self, *args):
        if len(args) == 1:
            self.name = args[0]

        elif len(args) == 2:
            self.name = args[0]
            self.age = args[1]

        elif len(args) == 3:
            self.name = args[0]
            self.age = args[1]
            self.gender = args[2]

st1 = student("Shrey")
print("name:",st1.name)
st2= student("Ram",26)
print(f'Name:{st2.name} and age: {st2.age}')
st3 = student("Shyam",26,"M")
print(f'Name:{st3.name},age:{st3.age} and gender:{st3.gender}')