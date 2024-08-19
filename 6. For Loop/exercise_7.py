#The following information is available:

#The ages of 5 students of the shift tomorrow.

#The ages of 6 students of the late shift.

#The ages of 11 students of the night shift.

#The ages of each student must be entered by keyboard.

#A) Obtain the average of the ages of each shift (three averages)

#B) Print these averages (average of each shift)

#C) Show on screen a message indicating which of the three shifts has a higher average age.

students_ages_tomorrow = 0
students_ages_late = 0
students_ages_night = 0
average_morning = 0
average_late = 0
average_night = 0
for x in range(1,6):
    students_ages_tomorrow = int(input('Please enter the age of the students of the shift tomorrow:'))
    average_morning = average_morning + students_ages_tomorrow / x

for y in range(1,7):
    students_ages_late = int(input('Please enter the age of the students of the late shift:'))
    average_late = average_late + students_ages_late / y
for z in range(1,12):
    students_ages_night = int(input('Please enter the age of the students of the night shift:'))
    average_night = average_night + students_ages_night / z

if average_morning > average_late and average_morning > average_night:
    print('Average morning is higher compared to the late and night shift')
else:
    if average_late > average_morning and average_late > average_night:
        print('Average late is higher compared to the morning and night shift') 
    else:
        print('Average night is higher compared to the morning and late shift')

print('Average morning')
print(average_morning)
print('Average late')
print(average_late)
print('Average night')
print(average_night)


