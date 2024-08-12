#Three different numbers are loaded by keyboard. 
#Show the largest of them on the screen.

first_number = int(input('Enter the number:'))
second_number =int(input('Enter the number:'))
third_number = int(input('Enter the number:'))

if first_number > second_number:
    if first_number > third_number:
        print('First number is bigger')
else:
    if second_number > first_number:
        if second_number > third_number:
            print('Second number is bigger')
        else:
            print('Third number is bigger')
