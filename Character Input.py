# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old. 
# Note: for this exercise, the expectation is that you explicitly write out the year (and therefore be out of date the next year).

name = input('enter your name: ')
print('your name is ' + name)

age = input('enter your age: ')
print('your age is ' + age)

year = 2022
age1 = int(age)
future = 100 - age1
age2 = future + year
print('you will turn 100 years old in' + age2)