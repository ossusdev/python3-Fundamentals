#Perform a program that reads the sides of n triangles, and inform:
#A) Of each of them, what type of triangle is it:
# equilateral (three equal sides),
# isosceles (two equal sides),
#or scalene (no equal side)
#B) Number of triangles of each type.


triangles = int(input('Enter the amount of triangles to evaluate:'))
equilateral_count = 0
isosceles_count = 0
scalene_count = 0

for x in range(triangles):
    side_1 = float(input('Enter the side:'))
    side_2 = float(input('Enter the side:'))
    side_3 = float(input('Enter the side:'))

    if side_1 == side_2 and side_3 ==side_2:
        print('equilateral')
        equilateral_count = equilateral_count + 1
    else:
        if side_1 == side_2 or side_2 == side_3:
            print('isosceles')
            isosceles_count = isosceles_count + 1
        else:
            print('scalene')
            scalene_count = scalene_count + 1

print('Equilateral:' + str(equilateral_count))
print('Isosceles:' + str(isosceles_count))
print('Scalene:' + str(scalene_count))


        

