

import random 
nota = random.randint(1, 10)
if nota >=6:
 print("Promoción directa, la nota es " + str(nota))
elif nota == 4 or nota == 5:
 print("Aprobado, la nota es " + str(nota))
else:
 print("Desaprobado, la nota es " + str(nota))
