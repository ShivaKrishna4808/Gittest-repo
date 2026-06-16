# raising exception ***

def login (username):
    if username == "":
        raise ValueError("Username cannot be empty")
    
    print("Login Successful")


try:
    login("")
except ValueError as e:
    print("Login Failed:",e)