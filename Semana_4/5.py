diez_enteros = [0] * 10
for i in range(10):
    diez_enteros[i] = int(input(f"Ingrese el {i+1} número: "))
posicion = None
numero_buscado = int(input("Ingrese un número a buscar: "))
for i in range(len(diez_enteros)):
    if diez_enteros[i] == numero_buscado:
        posicion = i + 1
        print(f"El número {numero_buscado} se encuentra en la posición {posicion}")
        break
if posicion is None:
    print(f"El número {numero_buscado} no se encuentra en lista")