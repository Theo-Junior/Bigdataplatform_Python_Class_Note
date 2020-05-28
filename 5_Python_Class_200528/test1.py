class Employee:
    name = "강감찬"
    count= 0
    def __init__(self, name="없음"):
        # print(name, self.count)
        Employee.count += 1
    def display(self, a=0):
        print(self.count,a)
    def __del__(self):
        print("delete")
class Employee2(Employee): #위에 있는 Employee클래스를 받기 때문에 Employee2의 display2함수를 호출해도 위의 클래스의 delete함수가 자동 실행됨
    def __init__(self):
        print("Employee2 생성자")
    def display2(self):
        print("Employee2 display2")
    def display(self, a=0,b=1):
        print(a,b)
# e = Employee()
# e.display()
# e.display(10)
# e.b = 10
# e2 = Employee()
# #e2.__del__
# e2.display()
# e2.__dict__
e2 = Employee2()
e2.display2()