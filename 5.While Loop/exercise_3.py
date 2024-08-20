#In a company there are n employees whose salaries range between $100 and $500,
#create a program that reads the salaries that each employee earns and reports how many employees earn between $100 and $300 and how many earn more than $300.
# In addition, the program must report the imports that the company spends on staff salaries.

employees = int(input('Enter the amount of employees:'))

x = 1
salary_between_100_and_300 = 0
salary_more_than_300 = 0

while x <= employees:
    salaries = int(input('Enter the salarie:'))
    if salaries >= 100 and salaries <= 300:
        salary_between_100_and_300 = salary_between_100_and_300 + 1
    else:
        if salaries > 300:
            salary_more_than_300 = salary_more_than_300 + 1
    
    x = x + 1

print('The amount of employees with a salary between 100 and 300 are:' + str(salary_between_100_and_300))
print('The amount of employees with a salary between higher to 300 are:' + str(salary_more_than_300))






