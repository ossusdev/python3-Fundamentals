###
#Make a program that reads four numerical values
# and report their sum and average.
###

num_1 = int(input('Please enter value:'))
num_2 = int(input('Please enter value:'))
num_3 = int(input('Please enter value:'))
num_4 = int(input('Please enter value:'))

sum_total = num_1 + num_2 + num_3 + num_4
sum_average = sum_total / 4

print('The sum of all values are:' + str(sum_total))
print('The average of the sum of all values is:' + str(sum_average))
