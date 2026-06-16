from dataclasses import dataclass, asdict
from typing import List

@dataclass
class student:
    name:str
    age:int
    grades:list[float]

students = student("Alice",29,[99.1,92.4,79.4])
student_dict = asdict(students)
print(student_dict)
