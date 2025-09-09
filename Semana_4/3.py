promediar = [0] * 6
suma = 0

for i in range(6):
    promediar[i] = float(input(f"Ingrese el {i+1} numero: "))
    suma += promediar[i]

print(f"El promedio es: {suma/6}")
