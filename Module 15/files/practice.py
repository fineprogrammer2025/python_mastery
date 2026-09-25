#Q1. create a new file, write some text to the file and read and print to the screen
#Q2. now create a new file, write some text to the file using a while loop, (at least 3 lines) and then read and print to the screen.

my_file = open("practice.txt", "a")
my_file.close()
my_file = open("practice.txt", "w")
my_file.write("This is a practice file")
my_file.close()

with open("practice.txt", "r") as my_file:
    content = my_file.read()
    print(content)
print("------------------------------")

another_file = open("practice_2.txt", "a")
another_file.close
another_file = open("practice_2.txt", "w")
another_file.write("This is another practice file")
another_file.close
another_file = open("practice_2.txt", "a")
x = 0
while x < 4:
    another_file.write(f"\nThis is another practice file {x}")
    x += 1
another_file.close
with open("practice_2.txt", "r") as another_file:
    content_2 = another_file.read()
    print(content_2)
print("------------------------------")