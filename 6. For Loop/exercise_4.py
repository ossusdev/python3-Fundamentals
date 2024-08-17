#Create a program that allows us to enter a value from 1 to 10
# and show us the multiplication table of the same (the first 12 terms)
#Example: If I enter 3, the values ​​​​3, 6, 9, up to 36 should appear on the screen.

value = int(input('Please enter value from 1 to 10:'))
for x in range(1,13):
    print(str(value) + 'x' + str(x) + '=' + str(value * x))
