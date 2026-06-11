class students:
    def __init__(self, name: str,age: int,percent:float):
        self.name = name
        self.age= age
        self.percent = percent

    def __repr__(self):
        return f"Student(Name = {self.name},age = {self.age}, percent = {self.percent})"
    def __eq__(self,other):
        if not isinstance(other,students):
            return NotImplemented
        return (self.name == other.name and self.age == other.age and self.percent == other.percent)
    
s1 = students("alice",20,90.1)
s2 = students("Bobby",22, 89.31)
print(s1)
print(s1==s2)