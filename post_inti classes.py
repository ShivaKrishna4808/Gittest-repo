from dataclasses import dataclass
@dataclass
class rectangle:
    width: float
    height: float
    area:float = 0.0





    def __post_init__(self):
     self.area = self.width *self.height

r = rectangle(5.0,10.0)
print(r)
print(f"Area of the rectangle :{r.area}")
    

