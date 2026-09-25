#Q1. create a nested for loop with the outer loop having 3 items and inner loop having 5 items

letters = ['a', 'b', 'c']
numbers = [1, 2, 3, 4, 5]
for letter in letters:
    print(letter)
    for number in numbers:
        print(number)
    print("\n")
print("--------------")