#Q1. create a while loop and print to the screeen "Great job" 3 time at least
#Q2. create a while loop and loop though 1 to 10 , but only print the first 5 on the screen utilizing the break statement

x = "Great job"
n = 0
while n < 5:
    print(x)
    n += 1
print("-------------------")   

numbers = 1
while numbers < 10:
    print(numbers)
    if numbers == 4:
        break
    numbers += 1
print("-------------------") 