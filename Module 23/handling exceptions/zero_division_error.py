#Try except blocks

#zero division error
# #without try except block
# print(0/0)
# print("------------------------")
#with try except block
# try:
#     print(0/0)
# except ZeroDivisionError:
#     print("You can't divide by zero")
# print("------------------------")

#value error
#without try except block
# number = int(input("Enter a number 1-10: "))
# print(f"you entered number {number}")
#with try except block
import sys
try:
    num = int(input("Enter a number 1-10: "))
except ValueError:
    print(f"please use numbers only")
    sys.exit()
print(f"you entered number {num}")