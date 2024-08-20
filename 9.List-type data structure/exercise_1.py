#Define by assignment a list with 8 integer elements. 
# count how many of these values store a value greater than 100.

list = [1,2,101,4,5,6,7,8]
count = 0
for x in list:
    if x > 100:
        count = count + 1
print('Values greater than 100')
print(count)

