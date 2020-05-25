# Call by Reference

def test_list(list1):
    list1.append(20)
    list1.append(30)
    print("Inside list = ", id(list1), list1)


list1 = [10, 30, 40, 50]
print(list1)

test_list(list1)
print("Outside list = ", id(list1), list1)

def add(x, y):
    return x + y

add(x=2, y=20)

def printName(*names):
    print(type(names))
    for name in names:
        print(name)

printName("이순신", "홍길동", "권율")

# 시스템 내장함수다..
print(globals())
print(__builtins__)

# 함수 타입 리턴..!
def test(*a):
    print(type(a))

test(1)
test("2")
test(1,2)
list((1,2))

# 이렇게 멀티 리턴이 된다..!
def add_and_subtract(a, b):
    return a+b, a-b

print(add_and_subtract(7,5))

# 튜플 리턴 확인이다. 
x, y = add_and_subtract(4,3)
print(x,y)

def msg(str):
    if str == "ok":
        print("ok")
        return
    print("next ok")

msg("good")
msg("ok")

data = [(1,2,3),(4,5,6),(7,8,9),(10,11,12)]

for x,y,z in data:
    print(x,y,z)