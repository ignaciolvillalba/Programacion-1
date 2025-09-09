numeros = [0] * 7
mayor = None
posicion = None
for i in range(len(numeros)):
    numeros[i] = int(input(f"Introduce el número {i + 1}: "))
    if mayor is None or numeros[i] > mayor:
        mayor = numeros[i]
        posicion = i +1
print(f"El número mayor es {mayor} y está en la posición {posicion}.")