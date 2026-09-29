with open("Names.txt", "w") as file:
    file.write("Dave\nBob\nSara\nMike\nTerry\nHenry")

x = open("Names.txt", "r")
print(x.read())
x.close()

with open("Message.txt", "x") as file:
    file.write("Welcome to the party! We hope you can make it. Food, fun and friends!")

y = open("Message.txt", "r")
print(y.read())
y.close()