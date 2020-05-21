""" a = 10;
name = '홍길동'
print(name)
b = c = 10 #multi assignment
print(b)
print(c)
a,b,c = 10,100,200
print(a)
print(b)
print(c) """

a = 10
b = 20
c = a + b
d = a * b
e = a / b
print(c)
print(d)
print(e)
print(b, c, d, e)
msg3 = "test2"
a1 = 200
a2 = 20.5
print(type(msg3), type(a1), type(a2))

msg1 = "Hello"
msg2 = "World"
msg3 = msg1 + msg2
print(msg3)
print(msg3*2)

msg4 = "Nice to meet you" #파이썬 숫자는 0부터 카운트한다
print(msg4[0]) #첫 문자 표현
print(msg4[-1]) # 마지막 문자 표현
print(msg4[0:3]) # 첫번째부터 네번째까지 문자 출력
print(msg4[:3]) #처음부터 네번째 문자까지 출력
print(msg4[0:]) #처음부터 모두 출력
print(msg4[1:5]) #두번째부터 6번째까지 출력
print(msg4[:])

msg5 = "HELLO"
print(msg5[0])
print(msg5[4])
print(msg5[:])
print(msg5[0:1]) #0과 1 사이의 값 H를 뿌려준다. E는 1과 2 사이의 값임.