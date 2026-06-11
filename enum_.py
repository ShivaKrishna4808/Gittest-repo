from enum import Enum

class subjects(Enum):
    ENGLISH = 'E'
    MATHS = 'M'
    GEOGRAPHY = 'G'
    SANSKRIT = 'S'

obj = subjects.SANSKRIT
print(type(obj))
print(obj.name)
print(obj.value)