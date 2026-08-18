
# Loops in python : if/elif/lse, for, while, break, continue, pass
# Write a program to find highest salary from the list of employees, it should be scalable to any number of employees in the list.
employees = [
    {"name": "Raghu",
     "age": 30,
     "salary": 10000},

    {"name": "Ravi",
     "age": 39,
     "salary": 31000},
     
    {"name": "Rakesh",
     "age": 35,
     "salary": 28000}
]

highest_salary = 0 # Start with 0 and update it whenever we find a higher salary.
highest_salary_employee = "" # Store the name of the employee with the highest salary found so far.

for employee in employees:
    if employee["salary"] > highest_salary:
        highest_salary = employee["salary"]
        highest_salary_employee = employee["name"]
print(f"Employee with the highest salary is:\n{highest_salary_employee}: {highest_salary}")

# For Loop
# write a code to find the emploees whos salary is greater than 20000
print("Employees earning more than 20000:\n")
for employee in employees:
    if employee["salary"] > 20000:
        print(f"{employee['name']}: {employee['salary']}")

# If-Else Loop
# Using the same employees list, print every employee and classify their salary
for employee in employees:
    if employee['salary'] > 20000:
        print(f"{employee['name']}: Above 20000")
    else:
        print(f"{employee['name']}: Below 20000")

# If-Elif-Else Loop
# Write a code to classify the salary into gropups
# Below 20000
# 20000 - 30000
# Above 30000

for employee in employees:
    if employee['salary'] < 20000:
        print(f"{employee['name']}: Below 20000")
    elif employee['salary'] <= 30000:
        print(f"{employee['name']}: 20000 - 30000")
    else:
        print(f"{employee['name']}: Above 30000")

# Use of 'Continue' statement
# Write a code where company wants to ignore employees earning below 20,000 and print only employee earn above it.
for employee in employees:
    if employee['salary'] <= 20000:
        continue #  Here we dont need 'else' statement here when python encounters 'contnue' it immediately skips the rest of the current iteration and moves to the next employee.
    print(f"Employee: {employee['name']}\nSalary: {employee['salary']}")

# Use of 'Break' statement
# Write a code that searches for an employee named "Ravi"
for employee in employees:
    if employee['name'] == "Ravi":
        print(f"Employee found: {employee['name']}\nSalary: {employee['salary']}")
        break

"""
continue vs break

continue --> Skip the current iteration
break --> Stop the entire loop

"""

# Challenge — combine everything
"""
Using employees list, write a program that:

Loops through all employees.
Skips employees earning 20,000 or less using continue.

If the employee is "Ravi", print:
Found Ravi

and stop the loop using break.
Otherwise, print the employee's name and salary.
"""
for employee in employees:
    if employee['salary'] <= 20000:
        continue
    if employee['name'] == "Ravi":
        print(f"Found {employee['name']}")
        break

# While Loop --> Keep doing something while a condition is true.
#Challenge 1 ---> while + user input
"""
Write a program that repeatedly asks the user to enter a number.
The program should continue asking until the user enters 0.
"""
"""
while True:
    number = int(input("Enter a number: "))
    if number == 0:
        print("program stopped")
        break
    print(f"You entered: {number}")
"""

# Challenge 2
"""
Write a program that:

1. Loops through the employees.
2. Skips anyone earning 20,000 or less.
3. Prints employees earning above 20,000.
4. If it finds "Amit", print:
"""

employees = [
    {"name": "Raghu", "age": 30, "salary": 10000},
    {"name": "Ravi", "age": 39, "salary": 29000},
    {"name": "Rakesh", "age": 35, "salary": 22000},
    {"name": "Amit", "age": 42, "salary": 45000},
]

for employee in employees:
    if employee['salary'] <= 20000:
        continue
    print(f"{employee['name']}: {employee['salary']}")
    if employee['name'] == "Amit":
        print(f"Found {employee['name']}")
        break # this is important here try without break and see the differnce

