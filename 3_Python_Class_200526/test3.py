a = 1
b = 10
def test(a):
    a = a + 1
    print(b, "b변수")
    return a

print(a, "1St")
a = test(a)
print(a, "2nd")

def add(a, b):
    """ add function """
    return a + b

add.__doc__ = "add function"
help(add)
