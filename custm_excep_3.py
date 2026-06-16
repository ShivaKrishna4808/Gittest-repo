class InvalidAgeerro(Exception):
    def __init__(self,age,message ="Age must be between 18 and 100"):
        self.age = age
        self.message = message
        super().__init__(self.message)

def set_age(age):
    if age < 18 or age>100:
        raise InvalidAgeerro(age)
    print(f"Age is set to {age}")


try:
    set_age(150)
except InvalidAgeerro as e:
    print(f"Invalid age: {e.age}.{e.message}")