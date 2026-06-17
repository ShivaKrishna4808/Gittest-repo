a = 10
b = 0
try:
    print("a/b")
    try:
        print("this is inner try block")
    except Exception:
        print("General Exception")
    finally:
        print("Inside inner finally block")
except ZeroDivisionError:
    print("Division by 0")
finally:
    print("Inside outer finally block")