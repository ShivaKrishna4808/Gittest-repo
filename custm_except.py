class MycustomError(Exception):
    pass

def risky_function():
    raise MycustomError("Something went wrong in risky_function")

try:
    risky_function()
except MycustomError as e:
    print(e)