str = "%10s" % "hi"
print(str)
print(len(str))

str2 = "%-10sjain." % "hi"
print(str2)
print(len(str2))

str3 = "%10.4f" % 3.42134234
print(str3)
print(len(str3))

str4 = "%0.4f" % 3.42134234
print(str4)
print(len(str4))

str5 = "I am Korean"
str6 = str5.split()
print(str6)
print(type(str6))

set1 = {1,2,3} # 세트는 집합과 동일한 값의 모임이다. 순서는 없고 {}로 표현한다. 중복 제거
list1 = ["홍길동", 100, 200] #리스트 명령은 일종의 보관창고, 컨테이너 역할을 하며 []로 표현한다. 타입 상관 없다.
tuple1 = (1,2,3) # 튜플은 리스트와 유사하나 ()로 표현하며 읽기 전용 = 수정 불가이다. 속도가 제일 빠르다.
dict1 = dict(a=1, b=2, c=3) # 사전은 가장 강력하고 편한다. 키 = 값의 쌍으로 구성되어있다. // 이는 dict생성자를 이용한 생성방법이고..
dict2 = {"a" : 1, "b" : 2, "c" : 3} # 이와 같이 생성이 가능하다..!
print(dict1)
print(dict1["a"])



print(list1)
list2 = [1, 2, 3] 
print(list2)
print(list1[0], list1[1], list1[2])

str6 - "%s는 %d원과 %d를 가지고 있습니다." % (list1[0], list1[1], list1[2])
print(str6)
list3 = [0,1,2,3,4,5]
print(list3[0:])
print(list3[:])
print(list3[2:4])
print(list3[:4])

list4 = ['짜장면', '짬뽕', '탕수육', '볶음밥', '군만두']
print(list4)
list4[0] = '팔보채'
print(list4)

list6 = [1, [1,2,3],4 ,[1,2,[1,2,3]]]
print(list6)
print(list6[1][2])
list6[3][2][2]

a = {'name' : 'pey', 'phone' : '1234', 'birth' : '1111'}
a.keys()
a.values()

# 이럴경우는 키만 먼저 출력
for i in a:
    print(i)

# 이럴경우는 밸류만 먼저 출력
for i in a:
    print(a[i])

days = {"Mon", "Tue", "Wed", "Thu", "Tue", "Mon"}
print(days)