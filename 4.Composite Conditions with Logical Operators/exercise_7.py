#An operator's salary and years of seniority are known.
# It is requested to create a program that reads the input data and reports:
#a) If the salary is less than 500 and their seniority is equal to or greater than 10 years, grant them a 20% increase, show the salary to be paid.
#b)If the salary is less than 500 but your seniority is less than 10 years, give you a 5% increase.
#c) If the salary is greater than or equal to 500, show the salary on the screen without changes.

salary = int(input('Enter the operator salary:'))
seniority = int(input('Enter the seniority:'))

if salary > 500 and seniority >= 10:
    increase = salary * 20 // 100
    print('The salary is:' + str(salary + increase))
else:
    if salary < 500 and seniority < 10:
        increase = salary * 5 // 100
        print('The salary is:' + str(salary + increase))
    else:
        if salary >= 500:
                    print('The salary is:' + str(salary))
()
