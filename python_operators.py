print("'Arithmetic Operators'")
x = 10
y = 5

Addition = x + y      #Addition operator
print(Addition)

Subtraction = x - y   #Subtraction operator
print(Subtraction)

Multiplication = x * y   #Multiplication operator
print(Multiplication)

Division = x / y     #Division operator
print(Division)

x = 10
y = 7
Modulus = x % y
print(Modulus)

x = 2 
y = 4
Exponent = x ** y
print(Exponent)
print()

print("'Comparison Operators'")
x = 2
y = 4
Equality =  x == y      #Equality operator
print(Equality)

x = 10
y = 5
Inequality = x != y     #Inequality operator
print(Inequality)

x = 10
y = 5
Greater = x > y     #Greater than operator
print(Greater)

Smaller = x < y     #Smaller than operator
print(Smaller)


print(x >= y)     #Greater than or equal to operator
print(x <= y)    #Smaller than or equal to operator
print()

print("'Assignment operators'")
x = 10
y = 5
z = x + y       #Assignment operator
print(z)

x += y      #Add&Assign 
print(x)

x -= y      #Subtract&Assign
print(x)

x *= y      #Multiply&Assign
print(x)

x = 10
y = 5
x /= y      #Divide&Assign
print(x)

x = 10
y = 7
x %= y      #Modulus&Assign
print(x)

x = 2
y = 5
x **= y     #Exponent&Assign
print(x)
print()

print("'Logical Operators'")
x = True
y = False

x and y    #And operator
print(x and y)

x or y     #Or operator
print(x or y)

not x      #Not operator    
print(not x)
print()

print("'Membership operators'")
x = [1, 2, 3, 4]
print(4 in x)       #In operator

print(4 not in x)   #Not in operator
print()

print("'Identity operators'")
x = ["red", "green", "blue", "black"]
y = ["red", "green", "blue", "black"]
z = x
print(x is z)       #Is operator  
print(x is not z)    #Is not operator


