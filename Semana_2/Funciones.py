def entero():
    numero = int(input("Introduce un número entero: "))
    return numero

def flotante():
    numero = float(input("Introduce un número flotante: "))
    return numero

def cadena():
    texto = input("Introduce una cadena de texto: ")
    return texto

def area_rectangulo(base, altura):
    area = base * altura
    return area

def area_circulo(radio):
    pi = 3.1416
    area = pi * (radio ** 2)
    return area

def par_o_impar(numero):
    if numero % 2 == 0:
        return "Par"
    else:
        return "Impar"
    
def par_o_impar_v2(numero):
    return numero % 2 == 0

def numero_gramder(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3

def potencia(base, exponente):
    for i in range(1, exponente):
        base *= base
    return base

def es_primo(numero):
    if numero < 2:
        return False
    for i in range(2, numero):
        if numero % i == 0:
            return False
    return True

def tabla_multiplicar(numero, min = 1, max = 10):
    for i in range(min, max + 1):
        print(f"{numero} x {i} = {numero * i}")


