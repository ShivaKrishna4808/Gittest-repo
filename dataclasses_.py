from dataclasses import dataclass

@dataclass
class student:
    name:str
    age:int
    percent:float

s1 = student("Shiva",20,91.5)
s2 = student("Rahul",22,86.91)

print(s1)
print(s1 == s2)
print(s1 != s2)