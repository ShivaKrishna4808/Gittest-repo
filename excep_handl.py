def divide(a,b):
    try:
        if b == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        

        result = a/b
        print("Result:",result)

    except ZeroDivisionError as e:
        print("Erro:",e)



divide(10,2)
divide(10,0)