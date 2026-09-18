name = "john doe"
# changing string casing using string associated methods; title(), upper(), lower(), strip(), lstrip(), rstrip().

# print(name.title())
# print(name.upper())
# name = "JOHN DOE"
# print(name.lower())

# Python Concatenation
l_name = "doe"
f_name = "john"
age = 40
full_name = f_name + ' ' + l_name
info = "My name is " + f_name.title() + " I am " + str(age) + " years old"
print(full_name.title())
print(info)

game = "    soccer    "
print(game.strip())
print(game.lstrip())
print(game.rstrip())

