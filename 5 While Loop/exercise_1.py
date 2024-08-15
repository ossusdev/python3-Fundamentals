#Write a program that requests to enter 10 student grades
# and informs us how many have grades greater than or equal to 7
# and how many have grades greater than or equal to 7 and how many have grades lower than or equal to 7.

loop_counter = 1
good_grade = 0
bad_grade = 0

while loop_counter <= 10:
    grade = int(input('Enter the grade:'))
    if grade >= 7:
        good_grade = good_grade + 1
    else:
        if grade < 7:
            bad_grade = bad_grade + 1
        else:
            print('Error')

    loop_counter = loop_counter + 1

print('Students with grades equal or greater than 7:' + str(good_grade))
print('Students with grades less or equal to 7:' + str(bad_grade))




