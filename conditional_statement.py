print("'If and Else Statements'")
print("script1")
if True:
    print("The condition is true")
print()

print("script2")
x = 50
y = 30
if x > y:
    print("x is greater than y")
print()

print("script3")
if x < y:
    print("x is less than y")
print()

print("script4")
if x < y:
    print("x is less than y")
else:
    print("x is greater than y")
print()
print()


print("'Elif Statements'")
print("script5")
x = 50
y = 30
z = 20
if x < y:
    print("x is smaller than y")
elif y < z:
    print("y is smaller than z")
elif x < z:
    print("x is smaller than z")
else:
    print("z is the smallest integer")
print()
print()

print("'Ternary Operator'")
print("script6")
car = "BMW"
isBMW = True if car == "BMW" else False
print(isBMW)
print()
print()

print("'Nesting conditional statements'")
print("script7")
x = 50
y = 30
z = 20

if x > y:
    print("x is greater than y")
    if x > z:
        print("x is greater than z")
    else:
        print("x is not greater than z")
elif y < z:
    print("y is smaller than z")
elif x < z:
    print("x is smaller than z")
else:
    print("z is the smallest integer")



