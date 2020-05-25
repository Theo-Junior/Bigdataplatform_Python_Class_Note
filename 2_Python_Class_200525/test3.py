a = int(input("첫번째 숫자 : "))
b = int(input("두번째 숫자 : "))
c = int(input("세번째 숫자 : "))

if a > b and a > c :
    print("a는 가장 크다.")

if b > a and b > c :
    print("b는 가장 크다.")

if c > a and c > b :
    print("c는 가장 크다.")

age = int(input("당신의 나이를 입력해주세요."))

if age >= 18:
    print("당신은 성인입니다.")

else : 
    print("당신은 어린입니다.")

#숫자를 입력받아 구구단을 출력하시오.

# j = int(input("원하는 구구단 ? : "))

# for i in range(1, 10):
#     while i<10 :
#         print('%d x %d  = %2d' % (j, i , j*i), end='')

i = 1
num = int(input("단수를 입력하세요 . "))
while i <= 9:
     print('%d x %d  = %2d \n' % (num , i , num*i))
     i = i + 1