letters = []
for letter in 'Python':
    letters.append(letter)
print(letters)

str = [letter for letter in 'Python']
print(str)

a = [1,2,3,4]
r = []
for n in a:
    r.append(n)
print(r)

a1 = [n for n in a if n% 2 == 0]
print(a1)

L = ['Apple', 'Orange', 'Banana']
for i in range(len(L)):
    print("Index : {0}, Value : {1}".format(i, L[i]))
