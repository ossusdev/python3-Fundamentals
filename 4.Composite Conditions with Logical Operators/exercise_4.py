#Write a program that asks you to enter the coordinate of a point in the plane, that is, 
# two integer values ​​x and y (non-zero).
#Then print on the screen in which quadrant said point is located. 
# (1st Quadrant if x &gt; 0 AND y &gt; 0, 2nd Quadrant: x &lt; 0 AND y &gt; 0, etc.)

x = int(input('Enter x value'))
y = int(input('Enter y value'))

if x > 0 and y > 0:
    print('First Quadrant')
else:
    if x < 0 and y > 0:
        print('Second Quadrant')
    else:
        if x < 0 and y < 0:
            print('Third Quadrant')
        else:
            print('Forth Quadrant')