sumar = [0] * 10
suma = 0

for i in range(10):
    sumar[i] = int(input(f"Ingrese el {i+1} número: "))
    suma += sumar[i]
print(f"La suma de los números es: {suma}")