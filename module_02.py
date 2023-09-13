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


absolute_value: abs(-12)
print('absolute value:',absolute_value)
print('absolute value:' +absolute_value)
print('absolute value:', abs(-12 ) )

print("I am",'25', "years old!")
print("apples", "oranges", "bananas", sep = "* ")

#variables.
name = 'rohini'
age = 18
pi = 3.14159
number = 123
is_a_student = True

print(type(name))
print(type(age))
print(type(pi))
print(type(number))
print(type(is_a_student))


print(f"My name is{name} and I am{age} years old.")
#output: My name is Rohini and I am 18 years

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

age = years_old + (float(months_old) /12)

print(age)