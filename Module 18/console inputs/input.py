txt = input("Can you see this? yes/no")
print("you said",txt)

#converting input to a number
txt = int(input("Enter a number: "))
print(f"The number given was {txt}")


#Troubleshooting Errors with TRY, EXCEPT

txt = input("Give me a num: ")
try:
    num = int(txt)
    print(f"the number given was {num}")
except ValueError:
    print("Please put in a real number")


salary = input("Enter your salary: ")
txt = "You make ${} a year"
print(txt.format(salary))