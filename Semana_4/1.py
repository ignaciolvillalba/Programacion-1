lista = [0] * 5

for i in range(5):
    lista[i] = int(input(f"Ingrese el {i+1} numero: "))

print("Los numeros ingresados son:")
for i in lista:
    print(i)