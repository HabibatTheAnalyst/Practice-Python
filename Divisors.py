# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?


user = input('enter any number: ')
mod = int(user) % 2
if mod == 0:
    print('you entered an even number.')
else:
    print('you entered an odd number.')


# If the number is a multiple of 4, print out a different message.
# Ask the user for two numbers: one number to check (call it num) and one number to divide by (check). 
# If check divides evenly into num, tell that to the user. If not, print a different appropriate message.

num =  input('enter any number: ')
check = input('enter another number: ')

if int(num) % int(check) == 0:
    print(num, 'divides evenly by', check)
else:
    print(num, 'does not divide evenly by', check)

