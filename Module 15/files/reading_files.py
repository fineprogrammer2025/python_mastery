a = open("demo.txt", "r")
print(a.read())
print("------------")
#or 
with open("demo.txt", "r") as a:
    print(a.read())
print("------------")

#READLINES 
a = open("demo.txt", "r")
print(a.readline())
a.close()
print("------------")
# Read parts of the test file in this case first 7 characters
a = open("demo.txt", "r")
print(a.read(7))
a.close()
print("------------")