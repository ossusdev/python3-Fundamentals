#A set of n person heights are entered per keyboard.
# Show the average height of people.

n=int(input("Cuantas personas hay:"))
x=1
sum=0
while x<=n:
    altura=float(input("Ingrese la altura:"))
    sum=sum+altura
    x=x+1
Prom=sum/n
print("Altura promedio")
print(Prom)
