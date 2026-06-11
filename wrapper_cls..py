def decorator_function(wrapped):
    class wrapper:
        def __init__(self,x):
            self.wrap = wrapped(x)
        def print_name(self):
            return self.wrap.name
    return wrapper
        


@decorator_function
class wrapped:
    def __init__(self,x):
        self.name = x

obj = wrapped("Tutorial points")
print(obj.print_name())