"""
Description: Module 02 Demonstration
Author: Ramanjot kaur
Date: September 12,2023
Usage: Run using button in the IDE
(integrated development environment)
"""

#this is an incline comment.


'''
This is a multiline comment.
It spans over multiple lines.
'''

# constants (python doesn't really have constants)
FEDERAL_TAX = 0.05
PI = 3.14


absolute_value: abs(-12)
print('absolute value:',absolute_value)
print('absolute value:' +absolute_value)
print('absolute value:', abs(-12 ) )

print("I am",'25', "years old!")
print("apples", "oranges", "bananas", sep = "* ")

#variables.
name = 'rohini'
age = 25
pi = 3.14159
number = 123
is_a_student = True

print(type(name))
print(type(age))
print(type(pi))
print(type(number))
print(type(is_a_student))


print(f"My name is{name} and I am{age} years old.")
#output: My name is Rohini and I am 25 years

print(f"The value of pi to two decimal places is {pi:.2f}.")
print(f"The number is {number:05}")
print(f"Hello,{name:> 10}")


#output" Hello,   Rohini
print(f"Hello,{name:>10} ")


#type conversion
age=18
current_salary = 67293.21

age_and_salary = age +current_salary

print(age_and_salary, type(age_and_salary))

months_old = "11"
years_old = 25

# age is implicity converted to integer
#months_old is explicitly converted into float
age = years_old + (float(months_old) / 12)

print(f"age as a float is{age:.3f}")

# $67,275.21
print(f"salary is: ${current_salary:,.2f}")

age = int(age)

print(age)

# maths
# + addition, concatenation
# - subtraction
# * multiplication
# / division

# regular division
result = 42/4  #10.5

#integer division
result = 42 // 4 #10

# modulus
result = 4 % 2   # 0
result = 3 % 2   # 1
result = 100 % 10  # 0
result = 101 % 10   # 1

# power
result = 2 ** 4  # 16

# assignment
result = 1 + 1

age = 25
age = age + 1
age += 1

countdown = 100

countdown -= 10


# shortcut operators
# the variable must already have a value assigned
# +=, -=, *=, /=, //=, %=, **=

# order of operations
# PEDMAS
# BEDMAS
# brackets or parentheses
# exponents
# Division
# Multiplication
# Addition
# Subtraction

result = 10 + 5 * 2 / 3 - 1

              # 10 / 3
              # 3.33333
              # 10 + 3.33333 - 1
              # 12.3333

print(result)

result  =  ((10 + 5) * 2) / 3 - 1 
print(result)

