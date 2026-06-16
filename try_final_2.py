balance = 5000

try:
    amt = int(input("Enter withdrawal amount: "))

    if amt>balance:
        raise Exception("Insufficient Balance")
    

    balance -= amt
    print("Withdrawal Successful")
    print("Remainig balance: ", balance)

except ValueError:
    print("Please enter a valid number")

except Exception as e:
    print("Transaction Failed:",e)

finally:
    print("Thank you for using our banking service")