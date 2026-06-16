class student:
    def __init__(self,name:str,age:int,percent:float):
        self.name = name
        self.age = age
        self.percent = percent

    def __repr__(self):
        return f"student(name={self.name},age={self.age},percent={self.percent})"
    def __eq__(self, other):
        if not isinstance(other,student):
            return NotImplemented
        return (self.name == other.name and self.age == other.age and self.percent == other.percent)
    
s1 = student("Shiva",20,91.1)
s2 = student("Rahul",92,98.1)
print(s1)
print(s1 == s2)
