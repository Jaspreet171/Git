Name = "Jaspreet"   #A string variable
Age = 22        #An integer variable
Weight = 50.5     #A float variable
Married = False     #A boolean variable

print(type(Name))
print(type(Age))
print(type(Weight))
print(type(Married))
print()


#PYTHON DATATYPES
print("Numeric types")
int_num =25     
print(type(int_num))

flt_number = 2.6554
print(type(flt_number))

cmp_number = 2 + 3j
print(type(cmp_number))

#You can define binary numbers in python by prefixing "0b" before the binary number
bin_num = 0b11010000    
print(bin_num)  #converted into integer when you try to print binary number
print(type(bin_num)) 
print()

print("Strings")
print("This is a string literal")

str_var = "This is a variable of string type"
print(str_var)
print(type(str_var))

str_mul = """Hell this string
spans on multiple lines
and this is the last line"""
print(str_mul)

single_quote = "This is a string 'single quoted' value"
print(single_quote)

double_quote = 'This is a string "double quoted" value'
print(double_quote)

#To access a single character within a  string
my_string = "Hello this is a simple string"
my_string[1]  
print(my_string[1])

#To calculate the length i.e., the no. of characters in your string using len() function
print(len(my_string)) 

#To concatenate two strings, you can use the addition operator(+)
string1 = "Hello how are you?"
string2 = "This is Mike"
print(string1 + string2)
print(len(string1 + string2))
print()

print("Boolean")    #can store either True or False
car = "Porsche"
print(car == "Porsche") 
print(car == "BMW")

car = "Honda"
isHonda = False

if car == "Honda":
    isHonda = True
else:
    isHonda = False
print(isHonda)
print()

print("Lists")  #collection of items of the same or different types

#creating a list
colors = ["Red", "Green", "Blue", "Orange"]
print(colors)
print(type(colors))

#We can also add items of different data types in a list
mixed_list = [20, "Female", "USA", True]
print(mixed_list)

#Accessing list elements
colors = ["Red", "Green", "Blue", "Orange"]
print(colors[1])

#You can also iterate through all the list items using a for loop
for col in colors:
    print(col)

#To find number of items ina list using len() function
print(len(colors))

#Adding elements to a list using append() method
colors = ["Red", "Green", "Blue", "Orange"]
colors.append("Black")
print(colors)

#Updating a list
colors = ["Red", "Green", "Blue", "Orange"]
colors[1] = "Yellow"
print(colors)

#Deleting a list item using remove() method
colors = ["Red", "Green", "Blue", "Orange"]
colors.remove("Green")
print(colors)

#using pop() method by passing list index
colors = ["Red", "Green", "Blue", "Orange"]
colors.pop(2)
print(colors)
#Using insert() method to add an element at specific position
colors = ["Red", "Green", "Blue", "Orange"]
colors.insert(2, "Yellow")
print(colors)
print()

print("Tuples")
#Tuples are immutable which means once created you cannot modify, update or delete items from a tuple

#creating a tuple
my_tuple = ("James", 25, "Male", True)
print(my_tuple)
print(type(my_tuple))

#Accessing tuple elements
print(my_tuple[1])

#We can also pass negative index no. to access items from the end of the tuple
print(my_tuple[-1])

#iterate through all the tuple items using a loop
for item in my_tuple:
    print(item)

print()

print("Dictionary")     #stores items in key-value pairs

#creating a dictionary
country_capitals = {"England" : "London", 
                    "France": "Paris",
                    "Japan": "Tokyo",
                    "India": "New Delhi"}
print(country_capitals)
print(type(country_capitals))

#Accessing dictionary items 
print(country_capitals["India"])

for k,v in country_capitals.items():
    print(k + " --> " + v)

#To iterate through all the dictionary keys, you can use the keys() method
for k in country_capitals.keys():
    print(k)

#To iterate through all the dictionary values, you can use the values() method
for v in country_capitals.values():
    print(v)

#Adding items to a dictionary
country_capitals["Greece"] = "Athens"
print(country_capitals)

#Modifying a dictionary item
country_capitals["Japan"] = "XYZ"
print(country_capitals)

#Deleting a dictionary item
country_capitals = {"England" : "London", 
                    "France": "Paris",
                    "Japan": "Tokyo",
                    "India": "New Delhi"}
del country_capitals["France"]
print(country_capitals)

#To remove all the items from dictionary by calling clear() method
country_capitals.clear()
print(country_capitals)
