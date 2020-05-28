try:
    a = int(input("a : "))
    b = int(input("b : "))
    c = a / b
    print(c)

except (ZeroDivisionError, Exception):
    print("Error")
# except Exception:
#     print("error")
else:
    print("ok")