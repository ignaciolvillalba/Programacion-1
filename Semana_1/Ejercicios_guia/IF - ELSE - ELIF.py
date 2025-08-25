#A partir del ingreso de la altura en centímetros de un jugador de baloncesto, el programa deberá determinar la posición del jugador en la cancha, considerando los siguientes parámetros:
#Menos de 160 cm: Base
#Entre 160 cm y 179 cm: Escolta
#Entre 180 cm y 199 cm: Alero
#200 cm o más: Ala-Pívot o Pívot

altura = int(input("Ingrese la altura del jugador (cm): "))
if altura < 160:
    posicion = "Base"
elif 160 <= altura <= 179:
    posicion = "Escolta"
elif 180 <= altura <= 199:
    posicion = "Alero"
else:
    posicion = "Ala-Pívot o Pívot"
print("La posición del jugador es:", posicion)

#Calcular una nota aleatoria entre el 1 y el 10 inclusive, para luego mostrar un mensaje según el valor:

import random 
nota = random.randint(1, 10)
if nota >=6:
 print("Promoción directa, la nota es " + str(nota))
elif nota == 4 or nota == 5:
 print("Aprobado, la nota es " + str(nota))
else:
 print("Desaprobado, la nota es " + str(nota))
