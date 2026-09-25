a = 1
while a < 6:
    print(a)
    a += 1
print("-----------------")
x = "Hello world"
y = 1
while y < 4:
    print(x)
    y += 1
print("-----------------")

# CONTINUE statement in while loops
x = 0
while x < 6:
    x += 1
    if x == 4:
        continue
    print(x)
print("-----------------")

y = 1
while y < 6:
    y += 1
    if y != 4:
        continue
    print(y)
print("-----------------")

#BREAK statement in while loop
a = 1
while a < 14:
    print(a)
    if a == 4:
        break
    a += 1