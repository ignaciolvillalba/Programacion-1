nombre = input("Ingrese el nombre del visitante:")
edad = int(input("Ingrese la edad del visitante:"))
atraccion = int(input("cuantas atracciones utilizará (maximo 3): "))
while atraccion  < 1 or atraccion > 3:
    print("Numero invalido")
    atraccion = int(input("cuantas atracciones utilizará (maximo 3): "))
costo_total = 0
atraciones_usadas = ""
for i in range(atraccion):
    opcion = input("Que atraccion desea visitar(Montaña rusa, Casa del terror, Carrusel): ")
    if opcion == "Montaña rusa":
        if edad >= 12:
            print("Puede ingresar")
            costo_total += 1500
            atraciones_usadas += "-Montaña rusa\n"
        else:
            print("No puede subir")
    elif opcion == "Casa del terror":
        if edad < 6:
            print("No puede subir a la Casa del terror")
        else:
            print("Puede subir")
            costo_total += 1200
            atraciones_usadas += "-Casa del terror\n"
    elif opcion == "Carrusel":
        print("Puede Subir al carrusel")
        atraciones_usadas += "-Carrusel"
        costo_total += 800
    else:
        print("Atraccion no valida")
        continue
print(nombre)
print(atraciones_usadas)
print("$", costo_total)
