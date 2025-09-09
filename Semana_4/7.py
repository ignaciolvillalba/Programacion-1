orden = [0] * 6
for i in range(6):
    orden[i] = int(input("Ingrese un número entero: "))
print("Los números en orden inverso son:")
for i in range(5, -1, -1):
    print(orden[i])
