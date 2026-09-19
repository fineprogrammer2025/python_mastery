#Q1. create 3 var & assign them values of 10, 20, 30, using one line of code

num1, num2, num3 = 10, 20, 30
print(num1, num2, num3)

#Q2. create 4 var & assign them values of 33, "car", 2,158, "hey" using one line of code

int_num, str_1, float_num, str_2 = 33, "car", 2.158, "hey"
print(int_num, str_1, float_num, str_2)

#Q3 create a multiple assignment operator and create 3 key/value pairs using the following as values (dave,41; bob,22; mark,38)

employees = {"Dave":41, "Bob":22, "Mark":38}
for key, value in employees.items():
    print(f"Employee {key} is {value} years old") 