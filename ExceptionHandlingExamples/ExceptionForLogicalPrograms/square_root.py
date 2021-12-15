# Python Program to calculate the square root

# To take the input from the user
num = float(input('Enter a number: '))
try:
    if num<0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
        print(ve)

num_sqrt = num ** 0.5
print('The square root of %0.3f is %0.3f'%(num ,num_sqrt))
