#Q1. Make sure to have a file to work with(like a text file). Copy that text file using the copy method, once copied, rename said file.
#Q2. Create a new txt file using python, write sone lines of text to that file. then copy that txt file using the copy method to another file name. Append some lines to the copied file. Print both txt files to the screen to compare


import shutil, os
new_file = open("Practice1.txt", "x")
with open("Practice1.txt", "w") as file:
    new_file.write("welcome to question1, note: i will be copied")
new_file.close()
src = "Practice1.txt"
dst = "practice1_destination.txt"
shutil.copy(src,dst)
os.rename("practice1_destination.txt", "new_practice1_destination.txt")
print("Q1 done")
print("------------------------------")

newer_file = open("Practice2.txt", "x")
newer_file = open("Practice2.txt", "w")
n = 0
while n < 3:
    newer_file.write("\n Hello world, this is practice 2.")
    n += 1
newer_file.close()

a = open("Practice2.txt", "r")
print(a.read) 
a.close()
print("Q2a done")
print("-----------------------------")

src_1 = "Practice2.txt"
dst_1 = "practice2_destination.txt"
shutil.copy(src_1, dst_1)
destination_file = open("practice2_destination.txt", "a")
a = 0
while a < 3:
    destination_file.write("\n I am superior.")
    a += 1
destination_file.close()
b = open("practice2_destination.txt", "r")
print(b.read())
b.close()
print("Q2b done")
print("----------------------------")


