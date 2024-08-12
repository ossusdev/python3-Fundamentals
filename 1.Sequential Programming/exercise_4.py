#
#Calculate the monthly salary of an operator knowing the number of hours worked
#and the value per hour.
#

hours_worked = int(input('Please enter the number of hours worked:'))
value_per_hour = int(input('Please enter the cost per hour worked:'))

salary = hours_worked * value_per_hour

print('The monthly salary of the workers is:' + str(salary))