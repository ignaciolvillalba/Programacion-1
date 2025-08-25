#Mostrar 10 repeticiones de números ascendentes desde el 1 al 10.
num = 1
while num < 11:
    print(num)
    num += 1
num = 10
#Mostrar 10 repeticiones de números descendentes desde el 10 al 1.
while num > 0:
    print(num)
    num -= 1
#Mostrar la suma de los números desde el 1 hasta el 10.
suma = 0
for x in range(1, 11):
    suma += x
print(suma)
#Mostrar la suma de los números pares desde el 1 hasta el 10.
suma = 0
for x in range(2, 11, 2):
    suma += x
print(suma)
#Solicitar el ingreso de 5 números, calcular la suma de los números ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
suma = 0
for x in range(5):
    num = int(input("ingrese un numero: "))
    suma += num
prom = suma / 5
print("La suma es " + str(suma))
print("El promedio es " + str(prom))
