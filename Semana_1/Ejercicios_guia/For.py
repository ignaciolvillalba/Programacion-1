#Mostrar los números ascendentes desde el 1 al 10
for i in range(1, 11):
    print(i)
#Mostrar los números descendentes desde el 10 al 1
for i in range(10, 0, -1):
    print(i)
#Ingresar un número. Mostrar los números desde 0 hasta el número ingresado.
numero = int(input("Ingrese un número: "))
for i in range(numero + 1):
    print(i)
#Ingresar un número y mostrar la tabla de multiplicar de ese número. Por ejemplo si se ingresa el numero 5
numero = int(input("Ingrese un número para ver su tabla de multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")
# Se ingresan un máximo de 10 números o hasta que el usuario ingrese el número 0.Mostrar la suma y el promedio de todos los números.
contador = 0
suma = 0 
while num != 0 and contador < 10:
    num = int(input("Ingrese un número (0 para terminar): "))
    suma += num
    contador += 1
if contador > 0:
    promedio = suma / contador
    print(f"Suma: {suma}, Promedio: {promedio}")
# Imprimir los números múltiplos de 3 entre el 1 y el 10.
for i in range(1, 11):
    if i % 3 == 0:
        print(i)
# Mostrar los números pares que hay desde la unidad hasta el número 50.
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
# Realizar un programa que permita mostrar una pirámide de números.
for i in range(1, 6):
    for x in range(1, i+1):
        print(x, end="")
    print()
#Ingresar un número. Mostrar todos los divisores que hay desde el 1 hasta el número ingresado. Mostrar la cantidad de divisores encontrados.
num = int(input("Ingrese un numero"))
contador = 0
for i in range(1, num+1):
    if num % i == 0:
        print(i)
        contador += 1
print(f"cantidad de divisores: {contador}")
#Ingresar un número. Determinar si el número es primo o no.
num = int(input("Ingrese un numero"))
contador = 0
for i in range(1, num+1):
    if num % i == 0:
        contador += 1
if contador == 2:
    print("Es primo")
else:
    print("No es primo")
#Ingresar un número. Mostrar cada número primo que hay entre el 1 y el número ingresado. Informar cuántos números primos se encontraron.
num = int(input("Ingrese un numero"))
contador = 0
contador_primos = 0
for i in range(1, num+1):
    for x in range(1, num+1):
        if i % x == 0:
            contador += 1
    if contador == 2:
        print(i)
        contador_primos +=1
print(f"se encontraron {contador_primos} numeros primos")