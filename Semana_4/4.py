mayor_que_cien = [0] * 8
contador = 0
for i in range(8):
    numero = int(input(f"Ingrese el {i+1} número: "))
    if numero > 100:
        mayor_que_cien[contador] = numero
        contador += 1

print(f"Numeros mayores que 100: {contador}")