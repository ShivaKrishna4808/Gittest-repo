from dataclasses import dataclass

@dataclass
class student:
    name:str
    age:int
    percent:float = 0.0

s1 = student("shiva",20)
s2 = student("manikanta",22,85.5)

print(s1)
print(s2)
