#Escribir una función verificar_acceso(edad) que reciba la edad de una persona y determine si  es mayor de edad (18 años o más) devolviendo un booleano.
#  Luego, el programa debe pedir la edad al usuario y mostrar un mensaje apropiado.
def verificar_acceso(edad):
    return edad >= 18
edad = int(input("Ingrese su edad: "))
if verificar_acceso(edad):
    print("Es mayor, puede acceder")
else:
    print("Es menor, no puede acceder")