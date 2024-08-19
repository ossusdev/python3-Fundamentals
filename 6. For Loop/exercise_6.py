# 10 integer values are loaded per keyboard. You want to know:
#A) The amount of negative values entered.
#B) The amount of positive values entered.
#C) The number of multiples of 15.
#D) The accumulated value of the numbers entered that are even

negative_value = 0
positive_value = 0
multiply_15 = 0
multiply_2 = 0


for x in range(10):
    value = int(input('Please enter the value:'))
    if value < 0:
        negative_value = negative_value + 1
    else:
        if value > 0:
            positive_value = positive_value + 1
    if value % 15 == 0:
        multiply_15 = multiply_15 + 1
    else:
        if value % 2 == 0:
            multiply_2 = multiply_2 + 1

print('negative_value:')
print(negative_value)
print('positive_value')
print(positive_value)
print('multiply_15')
print(multiply_15)
print('multiply_2')
print(multiply_2)


