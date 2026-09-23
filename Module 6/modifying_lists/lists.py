employees = ["john", "sam", "kate", "dan"]
ages = [20, 40, 23, 34]
#add to list
employees = employees + ["ella"]
print(employees)
#OR
employees.append("jim")
print(employees)
#OR
employees.insert(3,"steve")
print(employees)
print("------------------------")

#add two diff list
emp_info = employees + ages
print(emp_info)
print("------------------------")

#remove from list
del employees[2]
#this removes kate
print(employees)
#OR 
emp_info.remove(40)
print(emp_info)
print("------------------------")

#looping through a list
for item in emp_info:
    print(item)
print("------------------------")

#determine if an item is present in a list
if "john" in employees:
    print(employees)
    employees.remove("john")
    print(employees)
    print("john was here now he is not heehehe")
print("------------------------")
 
#determine the length of a list
length_employees = len(employees)
print(length_employees)