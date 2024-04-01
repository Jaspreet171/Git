print("'For loop'")
for i in range(10):
    print("Hello")
print()

for i in range(10):
    print(i)
print()

print("Table of 6 using for loop")
for i in range(10):
    print("6 x",i+1, "=",6*(i+1))
print()

for _ in range(10):     #_ is used when we don't want to use the variable
    print("Hello World")
print()

days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
for d in days:
    print(d)
print()
print()

print("'While loop'")
j = 0

while j<10:
    print("hello world")
    j += 1
print()

j = 0
while j<10:
    print("6 x",j+1, "=",6*(j+1))
    j += 1
print()
print()

print("'Nested Loops'")
for i in range(5):
    for j in range(5):
        print(i, "-", j)
print()

print("'Continue Pass & Break Statements'")
for i in range(10):
    if i == 5:
        continue
    print(i)
print()

for num in range(21):
    if num%2 != 0:
        continue
    else:
        print(num)
print()

