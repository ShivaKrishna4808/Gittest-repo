a =10
b=0
try:
    print("this outer try block")
    try:
        print("a/b")
    except KeyError:
        print("Key Error")
    finally:
        print("Inside inner finally block")

except ZeroDivisionError:
    print("Division by 0")
finally:
    print("Inside outer finally block")