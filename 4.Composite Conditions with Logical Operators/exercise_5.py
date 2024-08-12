

salary = int(input('Please enter the salary:'))
years_working = int(input('Please enter the amount of years working'))

if salary < 500 and years_working >= 10:
    salary_raise = (salary * 20) / 100
    salary = salary + salary_raise
    print('The new salary is' + str(salary))
else:
    if salary < 500 and years_working >= 10:
        salary_raise = (salary * 5) / 100
        salary = salary + salary_raise
        print('The new salary is' + str(salary))
    else:
        if salary >= 500:
            print('The new salary is' + str(salary))
