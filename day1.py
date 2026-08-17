"""
# Print first code
name = "Python"
print("Learn", name)

# Python is case sensitive
name1 ="python"
print(name == name1) # output will be False

# Variables and Data Types
name = "Ravi"       #integer
age = 39            #string
salary = 50000.00   #float
is_employee = True  #boolean

print(type(name))
print(type(age))
print(type(salary))
print(type(is_employee))

# Operators: Arithmatic, Comparison, Logical
#Arithmatic operators
a = 10
b = 4

print(a+b)
print(a-b)
print(a*b)
print(a/b)  # result will be float
print(a//b) # result will be round number and no decimals
print(a%b)  # result will be remainder
print(a**b)

#Comparison operators
x = 15
y = 19

print(x == y)
print(x != y)
print(x > y)
print(x < y)
print(x >= y)
print(x <= y)

#Logical operators: AND, OR, NOT
age = 39
salary = 50000

print(age > 25 and salary > 45000)
print(age > 35 or salary > 90000)
print(not age > 35)

# Take input from the user
college = input("enter your college name: ")
print(" You entered your college name as", college)

cgpa = input("enter your cgpa rank: ")
print("you entered cgpa rank: ", cgpa)
print(type(cgpa))   # by default input from user is considered as a string

cgpa_ = float(input("enter your cgpa rank: ")) # converting user input to float (if type integer then it will throw an error)
print(type(cgpa_))

"""
# ------------------------------------------------
"""
# Conversions: 
# 1.Type Conversion (python interpreter does it automatically also known as 'implicit')
lucky_num = input("enter your lucky number: ")
print("by default python interpreter consider it as string: ", type(lucky_num))
print("here interpreter converting input to float and then doing addition: ", type(1 + 2.5))
print("here interpreter converting float to integer and then doing addition: ", type(1 + int(2.5)))

# 2.Type Casting (we as a developer do conversion also known as 'explicit')
lucky_number = lucky_num
print("its still a string:", type(lucky_number))
print("here we are converting string to interger and float to integer:", int(lucky_number) + int(2.5))
print("here interpreter convert 2.5 to 2 and then addition: ", int(lucky_number) + int(2.5))

"""

"""
# Challenge 1: Write a program that takes two numbers and prints : addition, substraction, multiplication, division and remainder

a = int(input("eneter number 1: "))
b = int(input("eneter number 2: "))

addition = a+b
substraction = a-b
multiplication = a*b
division = a/b
remainder = a%b

print("addition of a and b is: ", addition)
print("substraction of a and b is: ", substraction)
print("multiplication of a and b is: ", multiplication)
print("division of a and b is: ", division)
print("remainder of a and b is: ", remainder)

# Challenge 2: Write a program that takes user age then calculate approx. what year they were born
age = int(input("enter your current age: "))
current_year = 2026
print("you were born in the year: ", current_year - age)

"""

# Challenge 3: Create a salary calculator
Basic = int(input("enter your basic component: "))
Hra = int(input("enetr hra component: "))
Transport = int(input("eneter transport allowance: "))
Other = int(input("enter other allowance: "))

Gross_Salary = Basic + Hra + Transport + Other
print("Your Gross Salary is: ", Gross_Salary)