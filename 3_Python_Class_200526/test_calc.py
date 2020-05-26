import calc as cp

c = cp.add(1,2)
b = cp.subtract(5,3)
print(c)
print(b)

from calc import add
c3 = add(3,5)
print(c3)

from calc import *
c6 = add(5,6)
c7 = subtract(8,8)
print(c6, c7)