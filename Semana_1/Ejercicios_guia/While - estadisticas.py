#Mostrar 10 repeticiones de numeros ascendentes desde el 1 al 10.

num = 1
while num < 11:
    print(num)
    num += 1
num = 10
#Mostrar 10 repeticiones de numeros descendentes desde el 10 al 1.

while num > 0:
    print(num)
    num -= 1
#Mostrar la suma de los numeros desde el 1 hasta el 10.

suma = 0
for x in range(1, 11):
    suma += x
print(suma)
#Mostrar la suma de los numeros pares desde el 1 hasta el 10.

suma = 0
for x in range(2, 11, 2):
    suma += x
print(suma)

#Solicitar el ingreso de 5 numeros, calcular la suma de los numeros ingresados y el promedio. Mostrar la suma y el promedio por pantalla.
suma = 0
for x in range(5):
    num = input("ingrese un numero: ")
    suma += float(num)
prom = suma / 5
print("La suma es " + str(suma))
print("El promedio es " + str(prom))

#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números ingresados y el promedio de los mismos

suma = 0
notas = 0
while True:
    num = input("Ingrese el numero que quiere sumar: ")
    if num == "":
        break
    suma += float(num)
    notas += 1
promedio = suma / notas
print(f"La suma es {suma}")
print(f"El promedio es {promedio}")

#Solicitar al usuario que ingrese números (hasta que no quiera ingresar más). Calcular la suma de los números positivos y el producto de los negativos.

suma = 0
producto = 1
while True:
    num = input("Ingrese un numero: ")
    if num == "":
        break
    elif float(num) > 0:
        suma += float(num)
    elif float(num) < 0:
       producto *= float(num)
print(f"La suma es: {suma}")
print(f"El producto es: {producto}")

#Ingresar 10 números enteros. Determinar el máximo y el mínimo

num = int(input("ingrese un numero: "))
max = num
min = num
for i in range(9):
    num = int(input("Ingrese un numero: "))
    if num > max:
        max = num
    elif num < min:
        min = num
print(f"El maximo es: {max}")
print(f"El minimo es: {min}")

#Solicitar al usuario que ingrese como mínimo 5 números. Calcular la suma de los números ingresados y el promedio de los mismos

suma = 0
contador = 0
while True:
    num = input("Ingrese un numero: ")

    if num == "":
        if contador >= 5:
            break
        else:
            print("Debes ingresar al menos 5 numeros")
            continue

    suma += int(num)
    contador += 1
prom = suma / contador
print(f"La suma es: {suma}")
print(f"El promedio es: {prom}")

#Solicitar al usuario que ingrese 5 números como mínimo y como máximo 10. Calcular la suma de los números ingresados y el promedio de los mismos.

suma = 0
contador = 0
while True:
    if contador == 10:
        print("Maximo alcanzado")
        break
    num = input("Ingrese un numero: ")

    if num == "":
        if contador >= 5:
            break
        else:
            print("Debes ingresar al menos 5 numeros")
            continue

    suma += int(num)
    contador += 1
prom = suma / contador
print(f"La suma es: {suma}")
print(f"El promedio es: {prom}")

#Realizar un programa que permita que el usuario ingrese todos los números que desee. Una vez finalizada la carga determinar:
#La suma acumulada de los números negativos.
#La suma acumulada de los números positivos.
#La cantidad de números negativos ingresados.
#El promedio de los números positivos.
#El número positivo más grande.
#El porcentaje de números negativos ingresados, respecto del total de ingresos.

suma_neg = 0
suma_pos = 0
contador = 0
contador_pos = 0
contador_neg = 0
porcentaje = 0
max_p = None
while True:
    entrada = input("Ingrese el numero que desee: ")
    if entrada == "":
        break
    num = float(entrada)
    contador +=1
    if num > 0:
        if num > max_p:
            max_p = num
        suma_pos += num
        contador_pos += 1
    else:
        suma_neg += num
        contador_neg += 1
if contador_pos > 0:
        promedio = suma_pos / contador_pos
else:
        print("Debe ingresar numeros positivos")
porcentaje = (contador_neg / contador) * 100
print(suma_neg)
print(suma_pos)
print(contador_neg)
print(promedio)
print(porcentaje)
