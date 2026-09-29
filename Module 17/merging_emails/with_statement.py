with open("Hello.txt", "w") as file:
    file.write("hey, there")

x = open("hello.txt", "r")
y = x.read()
print(y)
x.close()