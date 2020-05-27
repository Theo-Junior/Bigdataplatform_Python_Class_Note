from functools import reduce
import operator

class Calculator:

    def __init__(self):
        print("Turn on Calculator")

    def fnAdd(self, *arg):
        print("The result is : %d" % (sum(arg)))

    def fnMinus(self, *arg):
        print("The result is : %d" % (reduce(operator.__sub__, arg)))

    def fnMultiply(self, *arg):
        print("The result is : %d" % (reduce(operator.__mul__, arg)))

    def fnDivide(self, *arg):
        print("The result is : %d" % (reduce(operator.__truediv__, arg)))                 

    def __del__(self):
        print("Shut down Calculator")


if __name__ == '__main__':
    print("# Execute Check : Direct Execute \n")
    Calculator()

else :
    print("# Execute Check : Indirect Execute \n")
    Calculator()
        
calc = Calculator()

recycleFlag = True
while recycleFlag:

    num = int(input("\n\n ####### Calculator ######\n" \
      "#########################\n" \
      "# 1. Add\n" \
      "# 2. Minus\n" \
      "# 3. Divide \n" \
      "# 4. Multiply \n" \
      "# 5. Exit\n" \
      "#########################\n" \
      "Select what you want. [1-5] : "))

    strNum =  []
    intNum = [] 

    if num != 5:
        print("\n If you want input one more number, you should input Blank(Seperated by Space bar)")
        strNum = input("Input Number : ").split()
        intNum = tuple(map(int, strNum))

        if num == 1:
            calc.fnAdd(*intNum)
        

        elif num == 2:
            calc.fnMinus(*intNum)

        elif num == 3:
            calc.fnDivide(*intNum)

        elif num == 4:
            calc.fnMultiply(*intNum)

        elif num == 5:
            calc.__del__()

    else :
        recycleFlag = False
        del calc 