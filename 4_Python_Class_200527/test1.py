class Employee:
    name = "홍길동"
    age = 20
    def work(self):
        print("Employee\n--------\n",self.name, self.age, "\n\n")

emp = Employee()
emp.work()

class Student:
    count = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def study(self):
        print("Student_1\n--------\n", "name : %s \nage: %d" % (self.name, self.age), "\n\n")
    def displayCount(self):
        print(self.count)

stu1 = Student("이순신",30)
stu1.study()

class Student2:
    count = 0
    def __init__(self, name, age):
        self.count = self.count +1
    def displayCount(self):
        print("Student_2\n--------\n",self.count, "\n\n")



stu2 = Student2("강감찬", 50)
stu2.displayCount()

class Student3:
    count = 0
    def __init__(self):
        Student3.count = Student3.count +1
 
    def displayCount(self):
        print("Student_3\n--------\n", Student3.count, "\n\n")

stu3 = Student3()
stu3.displayCount()


# 아주 기본적인 생성이다. 메소드, 변수 제외하는..
class MyClass():
    pass

class Student4:
    def __init__(self):
        print("생성자")

    def study(self, name):
        print(name, "is studying")

stu4 = Student4()
stu4.study("KKK")

class Student5:
    def __init__(self, name, id, age):
        self.name = name
        self.id = id
        self.age = age

stu10 = Student5("QQQ", 100, 30)
print(getattr(stu10, 'name'))
setattr(stu10, 'name', "LLL")
print(getattr(stu10, 'name'))
print(hasattr(stu10, 'name'))

print(stu10.name)
delattr(stu10, 'name')
#print(stu10.name)

print(stu10.__dict__)
