"""
Make a program that requests the loading of 10 real values per keyboard.
 Show your sum at the end.
   Define several lines of comments indicating the name of the program,
   the programmer and the date of the last modification.
     Use the # character for the comments.
"""

#Sum of 10 values
#programmer: Ossus
#20 Aug 2024

sum = 0

for x in range(1,11):
    value = int(input('Enter value:'))
    sum = sum + value 

print('The sum is:')
print(sum)
