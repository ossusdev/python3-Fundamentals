"""
 Load two different names of people. 
 Show by screen then sorted alphabetically.
"""
name_1 = input('Enter name:')
name_2 = input('Enter name:')

if name_1 > name_2:
    print(name_1)
    print(name_2)
else:
    if name_2 > name_1:
        print(name_2)
        print(name_1)