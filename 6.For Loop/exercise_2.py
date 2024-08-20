#Develop a program that requests the loading of 10 numbers 
#and prints the sum of the last 5 values ​​entered.

sum = 0
for x in range(10):
    number = int(input('Input number:'))
    if x >=5:
        sum = sum + number 
print('The sum is:' + str(sum))

        
    
    