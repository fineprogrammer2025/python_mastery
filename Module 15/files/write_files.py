with open("demo.txt") as myfile:
    content = myfile.read()
    print(content)
print("-------------------------")
# 'a' this appends to the file
a = open("demo.txt", "a")
a.write("\nHere is another line in our text file")
a.close()
print("-------------------------")

with open("demo.txt") as myfile:
    content = myfile.read()
    print(content)
print("-------------------------")

# 'w' this overides the file 
a = open("demo.txt", "w")
a.write("what has happened now?")
a.close()
print("-------------------------")

with open("demo.txt") as myfile:
    content = myfile.read()
    print(content)
print("-------------------------")