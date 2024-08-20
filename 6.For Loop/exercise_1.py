#Create a program that allows you to load two lists of 15 values ​​each.
#Inform with a message which of the two lists has a greater accumulated value (messages "List 1 greater", "List 2 greater", "Lists equal")
#Keep in mind that there can be two or more repeating structures in an algorithm.


list_1 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
list_2 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
x  = 0
y = 0
cont_1 = 0
cont_2 = 0

for x in list_1:
    cont_1 = cont_1 + x
for y in list_2:
    cont_2 = cont_2 + y

if cont_1 > cont_2:
    print('List 1 is greater')
else:
    if cont_1 < cont_2:
        print('List 2 is greater')
    else:
         print('List 1 is equal to list 2')

