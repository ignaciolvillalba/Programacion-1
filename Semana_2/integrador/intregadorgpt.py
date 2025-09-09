#Ejercicio 1
altura = input("Ingrese la altura del jugador de basquet: ")
if altura < 160:
    print("El jugador es base")
elif 160 >= altura < 180:
    print("El jugador es escolta")
elif 180 >= altura < 200:
    print("El jugador es Alero")
elif altura >= 200:
    print("El jugador es Ala-pivot o Pivot")

import random
nota = random.randint(1, 10)
if 1>= nota <= 3:
    print("Desaprobado")
elif nota == 4 or nota == 5:
    print("Aprobado")
else:
    print("Aprobacion directa")

#Ejercicio 2
contador = 0
suma = 0
num_max = None
num_min = None
while contador < 5:
    num = input("Ingrese un numero")
    if num == "":
        print("ingrese un numero valido")
        break
    if num > num_max:
        num_max = num
    if num < num_min:
        num_min = num
    suma += num
promedio = suma / contador
print(f"La suma de los numeros es: {suma}\nEl promedio de los numeros es: {promedio}\nEl maximo es: {num_max}\nEl minimo es: {num_min}")

#Ejercicio 3
nota = 5
color = "verde"
while True:    
    note = input("Ingrese una notra entre 1 y 10: ")
    col = input("Ingrese un colo (Rojo, azul o verde): ")
    if note == nota and color == col:
        print("Clave correcta")
        break
    else:
        print("Incorrecto, ingrese de nuevo")

#Ejercicio 4
n = input("Ingrese un numero:")
for i in range(1, n+1):
    print(i)
for i in range(1, n+1):
    if i // 2 == 0:
        print(i)
#aca falta la piramide pq no supe como hacerlo


#Ejercicio 5

def es_par(num):
    if num / 2 == 0:
        print("Es par")
    else:
        print("Es impar")

def nummax(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3
    
def tabla(num, inicio=1, fin=10):
    for i in range(inicio, fin + 1):
        print("{num} * {i} = " + num * i)

def es_primo(num):
    if num < 2:
        print("No es primo")
    for i in range (1, num +1):
        if num % i == 0:
            print("Es primo")
        else:
            print("No es primo")

def primos(num):
    contador = 0
    for i in range(1, num+1):
        if num % i == 0:
            print(i)
            contador += 1
    print(f"Primos encontrados: {contador}")

#Ejercicio 6
# creo que este ejercicio no esta bien desarrolado pero entiendo lo que quisisite hacer