#Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Tendrá intentos indeterminados.
clave = "contraseña"
while True:
    cl = input("ingrese la clave: ")
    if cl == "contraseña":
        print("clave correcta")
        break
    else:
        print("clave incorrecta intente nuevamente")

#Pedir el ingreso de una clave. Validar que el ingreso del usuario sea correcto. Solo tendrá 3 intentos.

clave = "contraseña"
contador = 0
while contador < 3:
    cl = input("ingrese la clave: ")
    if cl == "contraseña":
        print("clave correcta")
        break
    else:
        print("clave incorrecta intente nuevamente")
        contador += 1

#Pedir al usuario el ingreso de una nota. La misma debe estar comprendida entre 1 y 10 inclusive.

while True:
    notra = int(input("ingrese una nota entre 1 y 10: "))
    if 1 <= notra <= 10:    
        print("nota correcta")
        break
    else:
        print("la nota debe ser entre 1 y 10")

#Solicitarle al usuario el ingreso de un color. Validar que el mismo sea Rojo, Verde o Azul.
while True:
    color = input("ingrese un color (Rojo, Verde o Azul): ")
    if color == "Rojo" or color == "Verde" or color == "Azul":
        print("color correcto")
        break
    else:
        print("color incorrecto, intente nuevamente")

#Una empresa dedicada a la toma de datos para realizar estadísticas y censos, nos pide realizar la carga y validación de datos.
#Los datos requeridos son:
#Apellido
#Edad, entre 18 y 90 años inclusive.
#Estado civil: “Soltero/a”, ”Casado/a”, “Divorciado/a” o “Viudo/a”.
#Número de legajo: valor numérico de 4 cifras, sin ceros a la izquierda.
#Una vez ingresados y validados los datos, mostrarlos por pantalla.

apellido = input("ingrese su apellido: ")
while True:
    edad = int(input("ingrese su edad (entre 18 y 90 años): "))
    if 18 <= edad <= 90:
        break
    else:
        print("edad incorrecta, intente nuevamente")
while True:
    estado_civil = input("ingrese su estado civil (Soltero/a, Casado/a, Divorciado/a o Viudo/a): ")
    if estado_civil == "Soltero/a" or estado_civil == "Casado/a" or estado_civil == "Divorciado/a" or estado_civil == "Viudo/a":
        break
    else:
        print("estado civil incorrecto, intente nuevamente")
while True:
    numero_legajo = input("ingrese su numero de legajo")
    if 1000 <= numero_legajo >= 9999:
        break
    else:
        print("El numero de legajo tiene que ser de 4 cifras y no comenzar con cero")
print(f"El apellido es: {apellido}")
print(f"La edad es: {edad}")
print(f"El estado civil es: {estado_civil}")
print(f"El numero de legajo es: {numero_legajo}")
