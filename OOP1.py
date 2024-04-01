print("'OOP in Python'")
print("To map with real world scenarios, we started using objects in code. \nThis is called object oriented programming.")
print()

print("'Class & Object in python'")
#Class is a blueprint for creating objects.

#creating class
class Student:
    name = "Jaspreet kaur"

#creating object(instance)
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)
print()

class Car:
    color = "Black"
    brand = "BMW"
    name = "M5 cs"

car1 = Car()
print(car1.color)
print(car1.brand)
print(car1.name)
print()

print("'Constructor'")
'''
__init__ function
All classes have a function called __init__(), which is always executed when the object is being initiated.
'''
#creating class
class Student:

    #default constructor
    def __init__(self):
        pass

    #parameterized constructor
    def __init__ (self, fullname="Harsh", marks=100):
        self.name = fullname
        self.marks = marks
        print("adding new student in Database")

#creating object
s1 = Student("Jaspreet kaur", 97)
print(s1.name, s1.marks)

s2 = Student("ABC", 90)
print(s2.name, s2.marks)

s3 = Student()
print(s3.name, s3.marks)

'''
The self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class.
'''
print()
print()

print("'Class & instance'")
'''
Class.attr
obj.attr

class: Student  --> which is common so we use class name to access it and store it 1 time in memory.
different student objects: s1, s2, s3 
same college name: "ABC" for all students

parameters: name, marks
'''

class Student:
    college = "ABC"

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks 
    
    def display_student(self):
        print("Name: ", self.name)
        print("Marks: ", self.marks)
        print("College: ", Student.college) #accessing the attribute using class name

s1 = Student("Jaspreet Kaur", 9 )   #creating object of class Student with arguments
s1.display_student()    #calling method of class Student using object of that class
print()


class Student:
    college_name = "Nirma University"
    name = "anonymous"      #class attr
    def __init__ (self,fullname,marks):
        self.name = fullname    #obj attr > class attr 
        self.marks = marks

s1 = Student("Jaspreet", 97)
print(s1.name, s1.marks)

s2 = Student("Harsh", 99)
print(s2.name, s2.marks)

print(s2.college_name)   # print(Student.college_name)  # both are same
print()
print()

print("'Methods'")
'''
Methods are functions that belongs to objects

class : store 2 things --> data(attributes) and methods(functions)
Agar hamare pass Car name ka class h to usme car ke attributes honge jaise color, brand, model etc. 
aur car ke methods honge jaise start, stop, move etc.
'''

class Student:
    college_name = "Nirma University"

    def __init__ (self,fullname,marks):
        self.name = fullname  
        self.marks = marks

    def welcome(self):
        print("Welcome to Nirma University",self.name)

    def get_marks(self):
        return self.marks
    # calling the method using object of the class
    # s1 is an object of Student class 
    
s1 = Student("Jaspreet", 97)
s1.welcome()   
print(s1.get_marks())  
print()
print()

print("Q. Create student class that takes name & marks of 3 subjects as arguments in contructor. \nThen create a method to print average")
print()

class Student:
    def __init__ (self,name,marks): 
        self.name = name
        self.marks = marks
    
    def get_avg(self):
        sum = 0
        for value in self.marks:
            sum += value
        print("Hey", self.name, "your average score is:", sum/3)

s1 = Student("Tony Stark", [99, 98, 97])
s1.get_avg()
print()

s1.name = "Ironman"
s1.get_avg()
print()
print()

print("'Static Method'")
'''
Methods that don't use the self parameter (work at class level)
'''

class Student:
    @staticmethod #decorator
    def college():
        print("Nirma University") 
Student.college()  
print()
print()

print("'Abstraction'")
'''
Hiding the implementation details of a class and only showing the essential features to the user.
Or hiding unnecessary data from the user. 
'''
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False

    def start(self):
        self.clutch = True
        self.acc = True
        print("Car started")

car1 = Car()
car1.start()
print()
print()

print("'Encapsulation'")
'''
Wrapping data and function into a single unit(object)
'''
print("Q. Create Account class with 2 attributes - balance & account number. \nCreate methods for debit, credit & printing the balance.")
print()

class Account:
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc

    #debit method
    def debit(self, amount):
        self.balance -= amount
        print("Rs.",amount,"debited from your account")
        print("Total balance = ", self.get_balance())

    #credit method
    def credit(self, amount):
        self.balance += amount
        print("Rs.",amount,"credited to your account")
        print("Total balance = ", self.get_balance())


    #display balance
    def get_balance(self):
        return self.balance
acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000)
acc1.debit(10000)


    

