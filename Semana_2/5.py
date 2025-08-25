#Definir una función es_par(numero) que reciba un número y devuelva True si es par y False si
#es impar. Luego, el programa debe pedir un número y mostrar si es par o impar usando la función
def es_par(numero):
    return numero % 2 == 0
numero = input("Ingrese un numero: ")
if numero == True:
    print("El numero es par")
else:
    print("El numero es impar")