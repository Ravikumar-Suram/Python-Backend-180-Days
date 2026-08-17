# These four structures are native to the language, require no imports, and handle the vast majority of data management tasks:
# 1. Lists: Ordered, mutable collections that allow duplicate elements and can hold mixed data types.
# 2. Tuples: Ordered, immutable sequences used to store fixed collections of data that should not change.
# 3. Dictionaries (dict): Unordered (ordered by insertion since Python 3.7) mappings of unique, immutable keys to values.
# 4. Sets: Unordered collections of unique elements, perfect for eliminating duplicates and performing math operations like unions and intersections.

"""
LIST   → mutable + ordered + duplicates allowed

TUPLE  → immutable + ordered + duplicates allowed

SET    → mutable + unique values + unordered

DICT   → key/value pairs

"""

# Before starting with these data structures, lets understand better about strings, which are also a data structure in Python. 
# Strings are sequences of characters and can be manipulated using various methods.

# Part 1: Strings
# Strings are sequences of characters enclosed in single quotes, double quotes, or triple quotes.


name = "Ravi"
name2 = 'Ravi Suram'
name3 = '''Ravi'''
print(name, name2, name3)

# String indexing
"""
R   a   v   i
0   1   2   3
-4  -3  -2  -1
"""

print(name[0])  # R (positive indexing starts from 0)
print(name[1])  # a (positive indexing starts from 0)
print(name[::])  # Ravi (entire string)
print(name[-2])  # v (negative indexing starts from the end of the string)
print(name[:3])  # Rav (from start to index 3, excluding index 3)
print(name[1:])  # avi (from index 1 to end)
print(name[1:3])  # av (from index 1 to index 3, excluding index 3)
print(name[-3:])  # avi (negative indexing starts from the end of the string)
print(name[:-1])  # Rav (excluding last character)
print(name[::2])  # Rv (start with 0th index and take every 2nd character)
print(name[::-1])  # ivaR (reverse the string)
print(name[1:3:2])  # a (From index 1 to index 3, take every 2nd character)
print(name[1:3:-1])  # empty string



# Useful string methods
text = "Hello, World! Welcom to Python Programming  "
print(text.upper())  # (convert to uppercase)
print(text.lower())  # (convert to lowercase)
print(text.capitalize())  # (capitalize first letter)
print(text.title())  # (capitalize first letter of each word)
print(text.strip())  # (remove leading and trailing whitespace)
print(text.replace("H", "S"))  # (replace H with S)
print(text.split(","))  # ['Hello', ' World!']
print(text.find("World"))  # 7 (find the index of the first occurrence of "World")
print(text.count("l"))  # 3 (count the number of occurrences of "l")
print(text.startswith("Hello"))  # True (check if string starts with "Hello")
print(text.endswith("World!"))  # True (check if string ends with "World!")
print(text.isalpha())  # False (check if string contains only alphabetic characters)
print(text.isdigit())  # False (check if string contains only digits)
print(text.isalnum())  # False (check if string contains only alphanumeric characters)
print(text.islower())  # False (check if string is in lowercase)
print(text.isupper())  # False (check if string is in uppercase)
print(text.isspace())  # False (check if string contains only whitespace)
print(text.center(20, "*"))  # *****Hello, World!***** (center the string with padding)
print(text.ljust(20, "*"))  # Hello, World!***** (left justify the string with padding)
print(text.rjust(20, "*"))  # *****Hello, World! (right justify the string with padding)
print(text.zfill(20))  # 0000000000Hello, World! (pad the string with zeros on the left)

# String formatting
name = "Ravi"
salary = 50000
print(f"{name} works for Amazon and his salary is {salary}")


# Exercise 1
text = "Python is a great programming language"
print(text[0]) # prints first character of the string
print(text[-1]) # prints last character of the string
print(text[:6]) # prints first six characters of the string
print(text[-8:]) #prints last eight characters of the string
print(text.upper()) # prints the string in uppercase
print(text.lower()) # prints the string in lowercase
print(len(text)) # prints the length of the string includes spaces
print(text[18:30]) # prints characters from index 18 to 29



#Part 2: Lists
# A list stores multiple values, a list can contain different types of data.
# List is mutable (can be changed after creation). Lists are defined using square brackets [].

data = ["Ravi", 35, "Python", 3.8, True]

print(data[1])  # 35 (accessing the second element of the list)
print(data[-1])  # True (accessing the last element of the list)

data[2] = "Java"  # changing the third element of the list
print(data)  # ['Ravi', 35, 'Java', 3.8, True]

data.append(50000) # adding an element to the end of the list
data.insert(2, "Developer") # adding an element at a specific index
data.remove(3.8) # removing an element from the list
print(data)  #['Ravi', 35, 'Developer', 'Java', True, 50000]

data.pop()  # removing the last element of the list
data.pop(4)  # removing the fourth element of the list
print(data)  # ['Ravi', 35, 'Developer', 'Java']


numbers = [11, 2, 23, 4, 50]
print(numbers)  # [11, 2, 23, 4, 50]
print(len(numbers))  # 5 (length of the list)
print(sum(numbers))  # 80 (sum of the list)
print(max(numbers))  # 50 (maximum value in the list)
print(min(numbers))  # 2 (minimum value in the list)


# Exercise 2
fruits = ["apple", "banana", "cherry", "date"]

fruits.append("strwaberry") # adds strawberry to the end of the list
print(fruits)
fruits.append("kiwi") # adds kiwi to the end of the list
print(fruits)
fruits.pop(2) # removes item using index value
print(fruits)
fruits.remove("date") # removes item by value
print(fruits)
fruits[1] = "blueberry" # changes banana to blueberry
print(fruits)
print(len(fruits)) # prints the length of the list



# Part 3: Tuples
# A tuple is similar to a list, but it is immutable (cannot be changed after creation). Tuples are defined using parentheses ().
# Tuples are often used to store related pieces of data that should not change, such as coordinates or RGB color values.
tuples_ = ("Python", "SQL", "FastAPI", 5, 3.8, True)
print(tuples_)
#tuples_[0] = "Java"  # This will raise an error because tuples are immutable

# Exercise 3
database = ("localhost", 5432, "postgres")
#database[0] # print host 
#database[1] # 'tuple' object is not callable
#database[1] = 3306 # 'tuple' object does not support item assignment
print(database)


# Part 4: Sets
# A set stores unique values. Set is represented in {} brackets. 
# Important note set doesn't support indexation, check printing set multiple times.
# Sets automatically discard duplicate values and retain only unique values.
skills = {"Python", "SQL", "FastAPI", "python", "SQL"}
print(skills) # set is case sensitive

# Set operations : Union, Intersection, Common
backend = {"Django", "MySQL", "Kubernetis"}
frontend = {"Angular", "HTML", "CSS", "MySQL"}

print(backend | frontend) # everything from both the sets
print(backend & frontend) # common thing from both the sets
print(backend - frontend) # skills in backend but not frontend


# Exercise 4
company_a = {"Python", "SQL", "Docker", "AWS"}
company_b = {"Python", "MongoDB", "Docker", "Kubernetes"}

print(company_a | company_b) # all skills
print(company_a & company_b) # skills common to both
print(company_a - company_b) # skills only in company_a
print(company_b - company_a) # skills only in company_b


# Part 5: Dictionaries 
# A dictionary stores: Key:Value pair.

emp = {
    "name": "Ravi",
    "age": 30,
    "department": "IT",
    "salary": 60000,
    "experience": 5
}

print(emp)
print(f" Departmwnt is: {emp['department']}")
print(f" Salary is: {emp['salary']}")

emp["department"] = "Sales" # updating department
print(emp)

del emp["experience"] # removing experience (emp.pop("experience") also works)
print(emp)

# Dictionary methods
print(emp.values())
print(emp.items())
print(emp.keys())


# Day 2 : Challenge
# Create an employee profile: 

employee = {
    "name" : "Ravikumar",
    "age" : 35,
    "dept" : "IT",
    "salary" : 50000,
    "skills" : ["Python", "Django", "MySQL", "AWS"]
}

print(f"Employee: {employee['name']}") # print employee name
print(f"Dept: {employee['dept']}") # print employee department

print("Skills:")
employee["skills"].append("Docker") # add Docker to employee skills
for skill in employee["skills"]:
    print(skill)

employee["salary"] += (employee["salary"] * 0.10) # increse salary by 10 percent
print(f"Salary: {int(employee['salary'])}")

employee["experience"] = 10 # add experience to employee profile
print(f"Experience: {employee['experience']} Years")

employee["salary"]
employee.get("salary")

# make a list of employees and perform operations on them
employees = [
    {
        "name" : "Ravi",
        "age" : 35,
        "dept" : "IT",
        "salary" : 50000,
        "skills" : ["Python", "Django", "AWS"]
    },
    {
       "name" : "Amit",
       "age" : 51,
       "dept" : "marketing",
       "salary" : 85000,
       "skills" : ["public communication", "project management", "sales & marketing"] 
    },
    {
        "name" : "Priya",
        "age" : 32,
        "dept" : "finance",
        "salary" : 41000,
        "skills" : ["accounts", "bookkeeping", "tally"]
    }
]

# print all employees names
for emp in employees:
    print(emp['name'])

print(employees[0]['skills']) # print skills of Ravi

employees[0]['skills'].append('Docker')
print(employees[0]['skills'])

employees[1]['salary'] += employees[1]['salary'] * 0.10
print(employees[1]['salary'])

employees[2]['skills'].append("AWS")
print(employees[2]['skills'])

print(employees)

# find the highest paid employee
if employees[0]['salary'] > employees[1]['salary'] and employees[0]['salary'] > employees[2]['salary']:
    print(f"Highest paid employee: {employees[0]['name']}\nSalary: {employees[0]['salary']}")
elif employees[1]['salary'] > employees[0]['salary'] and employees[1]['salary'] > employees[2]['salary']:
    print(f"Highest paid employee: {employees[1]['name']}\nSalary: {employees[1]['salary']}")
else:
    print(f"Highest paid employee: {employees[2]['name']}\nSalary: {employees[2]['salary']}")


# print all employees names and salaries
for emp in employees:
    print(f"Employee: {emp['name']}\nSalary: {emp['salary']}\n")

