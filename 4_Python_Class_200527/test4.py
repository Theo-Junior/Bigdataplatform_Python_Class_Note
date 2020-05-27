class MyData:
    def __init__(self, a, b, c):
        __c = 10
        self.a = b
        self.b = b
        self.__c = c
    
    def displayData(self):
        print(self.a, self.b)

    def __diplayData2(self):
        print("Nothing")
    
    def __del__(self):
        print("Delete")

myData = MyData(1, 2, 3)
print(myData.a)
myData.displayData()

