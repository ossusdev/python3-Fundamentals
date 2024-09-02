#Store in a list the salaries (float values) of 5 operators. 
#Print the list and the average salary.
sueldos=[]
suma=0
for x in range(5):
    valor=float(input("salary:"))
    sueldos.append(valor)
    suma=suma+valor

print("lists")
print(sueldos)
promedio=suma/5
print("average of salary:")
print(promedio)

