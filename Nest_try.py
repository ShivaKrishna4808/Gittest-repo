a =10
b =0
try:
    print(a/b)
except Exception:
    print("General Exception")
finally:
    print("Inside Outer Finally Block")