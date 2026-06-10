# Multiple Inheritence 




# class divison:
#     def __init__(self,a,b):
#         self.n=a
#         self.d=b

#     def divide(self):
#         return self.n/self.d
#     class modulus:
#         def __init__(self,a,b):
#             self.n=a
#             self.d=b
#         def mod_divide(self):
#             return self.n%self.d
        
# class div_mod(divison,modulus):
#     def __init__(self, a, b):
#         self.n = a
#         self.d=b

#     def div_and_mod(self):
#         divval = divison.divide(self)
#         modval = modulus.mod_divide(self)
#         return (divval,modval)



class division:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def divide(self):
        return self.n / self.d


class modulus:
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def mod_divide(self):
        return self.n % self.d


class div_mod(division, modulus):
    def __init__(self, a, b):
        self.n = a
        self.d = b

    def div_and_mod(self):
        divval = division.divide(self)
        modval = modulus.mod_divide(self)
        return (divval, modval)


# obj = div_mod(10, 3)
# print(obj.div_and_mod())

x=div_mod(10,3)
print ("division:",x.divide())
print ("mod_division:",x.mod_divide())
print ("divmod:",x.div_and_mod())