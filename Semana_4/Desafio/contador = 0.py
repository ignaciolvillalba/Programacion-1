contador = 0
while contador < 2:
    numero = int(input("Ingrese un numero: "))
    if numero not in range(-1000, 1001):
        print("Numero fuera de rango")
        continue
    contador +=1