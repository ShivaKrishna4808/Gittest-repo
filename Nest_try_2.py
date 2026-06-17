a = 10
b = 0
try:
    print(a/b)
    try:
        print("This is inner try block")
    except Exception:
        print("General Exception")
    finally:
        print("Inside inner Finally Block")

except ZeroDivisionError:
    print("Division by 0")
finally:
    print("Inside outer finally block")