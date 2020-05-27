class Employee5:
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee5.empCount += 1
    def displayCount(self):
        print("Employee %d" % Employee5.empCount)
    
    def displayEmployee(self):
        print("name : ", self.name, ", salary : ", self.salary)

emp1 = Employee5("KKK", 2000)
emp1.displayCount()
emp1.displayEmployee()

emp2 = Employee5("LLL", 3000)
emp2.displayCount()
emp2.displayEmployee()

print(Employee5.__dict__)
