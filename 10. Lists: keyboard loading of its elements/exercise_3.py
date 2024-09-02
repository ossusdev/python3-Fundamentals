"""
A company has two shifts (morning and afternoon) in which 8 employees work (4 in the morning and 4 in the afternoon)
Make a program that allows you to store the salaries of the employees grouped in two lists.
"""

morning_list = []
afternoon_list = []
print('Salary morning')
for x in range(4):
    salaries = float(input('Please enter the salary:'))
    morning_list.append(salaries)
print('Salary afternoon')
for y in range(4):
    salaries = float(input('Please enter the salary:'))
    afternoon_list.append(salaries)

print('Salaries per morning:')
print(morning_list)

print('Salaries per afternoon:')
print(afternoon_list)
