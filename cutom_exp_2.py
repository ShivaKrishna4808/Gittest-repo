class InvalidMarksError(Exception):
    pass

def check_marks(marks):
    if marks < 0 or marks>100:
        raise InvalidMarksError("Marks should be between 0 and 100")
    
    print("Valid marks: marks")

try:
    check_marks(180)

except InvalidMarksError as e:
    print("Error:",e)
