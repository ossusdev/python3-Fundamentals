#Three numbers are entered by keyboard, 
#if at least one of the entered values ​​is less than 10,
#print on the screen the legend "Some of the numbers are less than ten."

first_number = int(input('Enter the number'))
second_number = int(input('Enter the number'))
third_number = int(input('Enter the number'))

if first_number < 10 or second_number < 10 or third_number < 10:
    print('Some of the numbers are less than ten.')
