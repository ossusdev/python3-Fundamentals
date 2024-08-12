#
#Three grades are entered for a student,
# if the average is greater than or equal to seven, 
# a "Promoted" message will be displayed.
#

grade_1 = int(input('Enter the grade:'))
grade_2 = int(input('Enter the grade:'))
grade_3 = int(input('Enter the grade:'))

average = (grade_1 + grade_2 + grade_3) / 3

if average >= 7:
    print('Promoted')
