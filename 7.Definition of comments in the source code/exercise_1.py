""" 
Make a program that requests the loading of integer values by keyboard and adds them up. 
Finish the load by entering the value -1. 
Leave the statement of the problem as a comment within the source code."""

#variables int sum and bool x
sum = 1
x = True

#while loop
while x:
    value = int(input('Enter value:'))
    sum = sum + value
    if value == -1:
        break

 #print in console the sum of the values   
print('Total of value is:')
print(sum)

    