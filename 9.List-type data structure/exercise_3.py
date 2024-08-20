#Define a list that stores the names of 5 people by assignment.
#Count how many of those names have 5 or more characters.

list = ['Gilberto' , 'Edur' , 'Lisas' , 'Kareen' , 'Tama']
count = 0
x = 0
while x < len(list):
    print(list)
    if len(list[x]) >= 5:
        count = count + 1

    x = x + 1


print('Names with 5 or more characters:')
print(count)