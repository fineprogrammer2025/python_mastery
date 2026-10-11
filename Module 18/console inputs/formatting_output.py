salary = input("Enter your salary: ")
txt = "You make ${} a year"
print(txt.format(salary))
print("----------------------")
#Parameters 
#{field_name:conversions}
string = "Dave teaches {} {}."
print(string.format("cyber", "security"))

sentence = "Dave loves {1} {3} and has {2} {0}."
print(sentence.format("kids", "cyber", 7, "security"))