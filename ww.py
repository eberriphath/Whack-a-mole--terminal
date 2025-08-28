# def Division(num1, num2):
#     while num2 != 0:
#         num1, num2 = num2, num1 % num2
#     return num1

# # Read input as two integers separated by space
# # a, b = map(int, input("Enter two numbers: ").split())

# # Print the GCF
# print(Division(24,56))

# #######################



numbers = [1, 2, 3, 4, 5]
total = 0

for num in numbers:
    total = total + num   # or total += num

print(total)


#############################
# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')



#################

# Print numbers until the user enters 0
number = int(input('Enter a number: '))

# iterate until the user enters 0
while number != 0:
    print(f'You entered {number}.')
    number = int(input('Enter a number: '))

print('The end.')


##################

# function definition
def find_square(num):
    result = num * num
    return result

# function call
square = find_square(3)

print('Square:', square)