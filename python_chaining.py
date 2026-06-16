class InvalidAgeError(Exception):
    pass
def get_age():
    try:
        age = int(input("Enter your age:"))

        if age < 0:
            raise ValueError("age cannot be negative")
        
        return age
    except ValueError as e:
        raise InvalidAgeError("Invalid age entered") from e
    
try:
    age = get_age()
    print("Your age is:",age)

except InvalidAgeError as e:
    print("Custom Error:",e)
    print("Original Error:",e.__cause__)