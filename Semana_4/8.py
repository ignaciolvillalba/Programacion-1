lista1 = [0] * 5
for i in range(5):
    lista1[i] = int(input("Ingrese un número para la lista 1: "))
lista2 = [0] * 5
for i in range(5):
    lista2[i] = int(input("Ingrese un número para la lista 2: "))
for i in range(5):
    if lista1[i] == lista2[i]:
        print("Los números son iguales")
    else:
        print("Los números son diferentes")