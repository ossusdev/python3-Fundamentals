#Three numbers are entered by keyboard,
# if all the values ​​entered are less than 10, print on the screen the legend "All numbers are less than ten."

first_number = int(input('Enter the number'))
second_number = int(input('Enter the number'))
third_number = int(input('Enter the number'))

if first_number < 10 and second_number < 10 and third_number < 10:
    print('All numbers are less than ten')
