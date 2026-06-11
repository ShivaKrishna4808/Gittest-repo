from enum import Enum

class subjects(Enum):
    English = 'E'
    Maths = 'M'
    Geography = 'G'
    Sanskrit = 'S'


for sub in subjects:
    print(sub.name,sub.value)