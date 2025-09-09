pares = [0] * 10
for i in range(10):
    num = int(input("Ingrese un número: "))
    if num % 2 == 0:
        pares[i] = 0
    else:
        pares[i] = num
print(pares)