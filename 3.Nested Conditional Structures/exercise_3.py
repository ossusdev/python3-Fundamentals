#
#Create a program that allows loading a positive integer of up to three digits
# and displays a message indicating whether it has 1, 2, or 3 digits.
# Show an error message if the number of figures is greater.
#

number = int(input('Please enter a number:'))

if number > 0:
    if number < 10:
        print('The number is 1 digit')
    else:
        if number > 9:
            if number < 100:
                print('The value has 2 digits')
            else:
                if number > 99:
                    if number < 10000:
                        print('It has 3 digits')
                    else:
                        print('Error')