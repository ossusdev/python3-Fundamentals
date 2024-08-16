#Show multiples of 8 up to the value 500.
#8 - 16 - 24, etc. should appear on the screen.

x = 1
while x <= 500:
    serie = x
    serie = serie * 8

    if serie > 500:
        break
    print(serie)
    x = x + 1
    
