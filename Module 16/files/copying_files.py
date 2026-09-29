import shutil
a = open("demo.txt", "x")
with open("demo.txt", "a") as file:
    file.write("Hello world")
print("done")
a.close
src = "demo.txt"
dst = "DavesDemo.txt"
shutil.copy(src,dst)