
#Create a program that asks you to load any date, 
#then verify if said date corresponds to Christmas.

date = input('Enter the date:')
month = input('Enter the month:')
year = input('Enter the year:')

if date == '25' and month == 'December' or month == 'december' and year == '2024':
    print('It is Christmas')
else:
    print('It is not Christmas')