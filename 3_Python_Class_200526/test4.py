file = open("file.txt", "w")
for i in range(1,6):
    data = "Hi\n"
    file.write(data)

print("writed")
print(file.name)
file.close()

file = open("file.txt", "r")
a = file.readlines()
print(a)