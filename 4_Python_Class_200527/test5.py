class Calc1:
    def Add(self, a, b):
        return a + b
    
class Calc2:
    def multiply(self, a, b):
        return a * b

class Calc3(Calc1, Calc2):
    def divide(self, a, b):
        return a / b

c = Calc3()
print(c.Add(1,2))
print(c.multiply(3,2))
print(c.divide(4,2))