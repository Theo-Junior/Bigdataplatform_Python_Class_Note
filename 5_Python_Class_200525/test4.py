num = int(input("메뉴를 선택해주세요.[1-4]"))
if num == 1:
    print("덧셈입니다.")
    a = int(input("첫번째 숫자를 입력해주세요. "))
    b = int(input("두번째 숫자를 입력해주세요. "))
    print('결과는 %d입니다.' %(a+b))
elif num ==2:
    print("뺄셈입니다.")
    a = int(input("첫번째 숫자를 입력해주세요. "))
    b = int(input("두번째 숫자를 입력해주세요. " ))
    print('결과는 %d입니다.' %(a-b))
elif num ==3:
    print("곱셈입니다.")
    a = int(input("첫번째 숫자를 입력해주세요. "))
    b = int(input("두번째 숫자를 입력해주세요. " ))
    print('결과는 %d입니다. ' %(a*b))
else :
    print("나눗셈입니다.")
    a = int(input("첫번째 숫자를 입력해주세요. "))
    b = int(input("두번째 숫자를 입력해주세요. " ))
    print('결과는 %d입니다. ' %(a/b))

letters = []
for letter in 'Python':
    letters.append(letter)

print(letters)
str = [letter for letter in 'Python']
print(str)
