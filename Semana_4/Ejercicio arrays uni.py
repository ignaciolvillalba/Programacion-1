def lista(num):
    listanueva = [0] * num
    return listanueva

def ingreso(n):
    lista = lista(n)
    for i in range(len(lista)):
        numero = int(input(f"Ingrese el numero {i+1}: "))
        lista[i] = numero
    return lista

def promedio(lista):
    suma = 0
    for i in lista:
        suma += i
    return suma / len(lista)

def promedio_positivos(lista):
    suma = 0
    for i in lista:
        if i > 0:
            suma += i
    return suma / len(lista)

def producto(lista):
    product = 1
    for i in lista:
        product *= i
    return product

def maximo(lista):
    maxim = lista[0]
    posicion = 0
    for i in range(len(lista)):
        if lista[i] > maxim:
            maxim = lista[i]
            posicion = i
    return posicion

def maximo(lista):
    maxim = max(lista)
    posiciones = []
    for i in range(len(lista)):
        if lista[i] == maxim:
            posiciones.append(i)
    print(f"El maximo es: {maxim}")
    print(f"Se encuentra en las posiciones: {posiciones}")

def reemplazar_nombres(lista_nombres, nombre_antiguo, nombre_nuevo):
    contador = 0
    for i in range(len(lista_nombres)):
        if lista_nombres[i] == nombre_antiguo:
            lista_nombres[i] = nombre_nuevo
            contador +=1
    return contador

def interseccion_arrays(lista1, lista2):
    interseccion = []
    for elemento in lista1:
        if elemento in lista2 and elemento not in interseccion:
            interseccion.append(elemento)
    print(interseccion)

def union(lista1, lista2):
    union = []
    for i in lista1 + lista2:
        if i not in union:
            union.append(i)
    print(union)

def diferencia(lista1, lista2):
    diferencia = []
    for i in lista1:
        if i not in lista2:
            diferencia.append(i)
    print(f"La diferencia es: {diferencia}")
    