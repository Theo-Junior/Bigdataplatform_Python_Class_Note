class Animal:
    def breath(self):
        print("Animal breath")

class Dog(Animal):
    def bark(self):
        print("Dog barking")

    def breath(self):
        print("Dog breathing")

d = Dog()
d.bark()
d.breath()

