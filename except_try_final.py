def divide_numbers():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))

        result  =num1/num2
        print("Result: ",result)


    except ValueError:
        print("Error: Please enter valid integers.")

    except ZeroDivisionError:
        print("Error: Cannot divide by zero.")

    finally:
        print("Program execution completed.")


divide_numbers()
                   