def calc_sum(a,b):
    sum = a + b
    print(sum)
    return sum
calc_sum(4,8)


#function definition
def calc_sum(a,b):      #parameters
    return a +b

sum = calc_sum(2,4)     #function call ; arguments
print(sum) 


def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()
print_hello()

output = print_hello()  
print(output)   #None

#avg of 3 numbers
def avg_num(a,b,c):
    avg_num = (a+b+c)/3
    print(avg_num)
    return avg_num

avg_num(2,4,6)

#Types of functions in python
''' built in functions in python 
print()     len()       type()      range()

user defined functions
Functions which are defined by the user are called user defined functions. They can be classified into two types: 
1. simple function : no parameters , no return value
2. parameterized function: with parameters and return value
'''
print()
print()

print("Q.1 WAF to print the length of a list(List is a parameter)")

cities = ["Delhi", "Mumbai", "Pune", "Bangalore", "Chennai", "Ahmedabad"]
heroes = ["Ironman", "Thor", "Hulk", "Captain America"]
def print_len(list):
    print(len(list))

print_len(cities)
print_len(heroes)
print()
print()

print("Q.2 WAF to print the elements of a list in a single line(list is the parameter)")

def print_list(list):
    for i in list:
        print(i, end=" ")
print_list(heroes)
print()
print()




print("Q.3 WAF to find the factorial of n(n is the parameter)")

def cal_fact(n):
    fact = 1 
    for i in range(1, n+1):
        fact *= i
    print(fact)

cal_fact(6)
print()




print("Q.4 WAF to convert USD to INR")

def converter(usd_val):
    inr_val = usd_val * 83
    print(usd_val,"USD =",inr_val,"INR")

converter(100)
print()
print()


print("'Recursion'")      #When a function calls itself repeatedly

def show(n):
    if (n == 0):
        return
    print(n)
    show(n-1)
show(5)
print()

def fact(n):
   if (n==0 or n==1):
    return 1
   return fact(n-1) * n
print(fact(4))
print()


print("Q.1 Write a recursive function to calculate the sum of first n natural numbers.")
def calc_sum(n):
    if (n==0):
        return 0
    return calc_sum(n-1) + n

sum = calc_sum(5)
print(sum)
print()

print("Q.2 Write a recursive function to print all the elements of a list.")
def print_list(list, i):
    if (i==len(list)):
        return
    print(list[i])
    print_list(list, i+1)

fruits = ["Apple", "Banana", "Mango", "Grapes", "Orange"]
print_list(fruits, 0)
print()