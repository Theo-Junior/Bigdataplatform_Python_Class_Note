# class A:
#     def __init__(self,a):
#         self.a = a
#     def __add__(self,o):
#         return self.a + o.a
# a = A(1)
# b = A(2)
# c = a.__add__(b)
# c2 = a+b
# print(c, c2)

class Test:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __add__(self,v):
        return self.a + v.a, self.b + v.b

t = Test(1,2)
print(t)
t2 = Test(3,4)
print(t2)
t3 = t + t2
print(t3)
t4 = t.__add__(t2)
print(t4)

