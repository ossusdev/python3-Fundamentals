#
#Create a program that requests the keyboard loading of two numbers,
# if the first is greater than the second, report their sum and difference,
# otherwise report the product and division of the first with respect to the second.
#

first_value = int(input('Load the value:'))
second_value = int(input('Load the value:'))

if first_value > second_value:
    sum = first_value + second_value
    difference = first_value - second_value
    print('The sum is:' + str(sum))
    print('The difference is:' + str(difference))

else:
    product = first_value * second_value
    division = first_value / second_value
    print('The product is:' + str(product))
    print('The division is:' + str(division))
