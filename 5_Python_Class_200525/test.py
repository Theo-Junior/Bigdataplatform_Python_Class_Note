a=[1,2,3]
b=a
print(id(a),a)
print(id(b),b)

c=a[:]
c.append([1,2,3])

print(id(a), a)
print(id(c), c)

d=[[2,3],[1,2]]
e = d[:]
print(id(d),d)
print(id(e),e)

e[0].append(3)
print(id(d),d)
print(id(e),e)


import copy

f = copy.deepcopy(e)
f[0].append([1,2,3])
print(id(f), f)