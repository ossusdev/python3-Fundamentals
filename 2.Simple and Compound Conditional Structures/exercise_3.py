#A positive number of one or two digits (1..99) is entered by keyboard 
# and a message is displayed indicating whether the number has one or two digits.
#

number = int(input('Enter a number between 1 ..99:'))

if number < 10:
    print('It has 1 digit')
if number > 9:
    print('It has 2 digit')

