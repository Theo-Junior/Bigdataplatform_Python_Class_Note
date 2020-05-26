print(1)
print('hi guys')
a = 'Hello\n'

x = 0.2
print(x)
str(x)
print(str(x))
a = repr('hello\n')
print(a)

import sys
print("Welcome to", "python", sep="-", end="!", file=sys.stderr)

import sys
help(sys.stderr)

#파일 입출력 // Default is Read
f = open('file.txt', 'w') # Write
f.write('plow deep\nwhile sluggards sleep')
f.close()

f = open('file.txt', 'r') # Read
f.read()
print("file write", 'r') # Read
f.close()

f.close()

# 파일 입출력 확장
f = open('file.txt') # Read
f.read()

f.read()

f.tell() # 어디까지 읽었니..

f.seek(0) # 0으로 돌아가라.. (처음으로)

f.read() # 다시 읽으면 처음부터 읽게된다 Seek 때문에..ㅎ

f.seek(0)
f.readline()
f.readline()
f.seek(0)
f.readlines()
f.close()


# 문자열 포매팅
print("{0} is {1}".format("apple", "red"))
