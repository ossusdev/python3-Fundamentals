#Three values ​​are entered by keyboard, 
# if all are equal, the sum of the first 
# and the second is printed and this result is multiplied by the third.

first_number = int(input('Enter the number'))
second_number = int(input('Enter the number'))
third_number = int(input('Enter the number'))

if first_number == second_number and first_number == third_number :
    sum = first_number + second_number
    result = sum * third_number
    print('The sum of the first and second number is:' + str(sum))
    print('The result of the sum multiplied with the third number is:' + str(result))