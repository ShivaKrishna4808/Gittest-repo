from dataclasses import dataclass,field 
from typing import List
@dataclass
class course:
    name:str
    students:list[str] = field(default_factory=list)



course1 = course("Math")
course2 = course("Science",["ram","shiva"])

course1.students.append("Mani")
print(course1)
print(course2)
