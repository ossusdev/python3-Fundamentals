#
# An integer value is entered by keyboard, 
# show a legend indicating if the number is positive,
# negative or null (i.e. zero)
#

value = int(input('Enter the value:'))

if value > 0:
    print('The value is positive')
else:
    if value < 0:
        print('Value is negative')
    else:
        print('Value is null')