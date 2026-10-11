a = open("demo.txt", "r")
print(a.read())
a.close()
print("------------")
#or Reading files - with 
with open("demo.txt", "r") as a:
    print(a.read())
print("------------")
with open("demo.txt", "r") as myfile:
    contents = myfile.read()
    print(contents)
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