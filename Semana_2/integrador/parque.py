def mostrar_atracciones():
    print("1.Montaña rusa\n2.Casa del terror\n3.Carrusel")
    atraccion = input("Elija la atraccion que quiere usar: ")
    return atraccion
def puede_subir(edad, atraccion):
    if atraccion == "Montaña rusa":
        if edad >= 12:
            return True
        else:
            print("No puede subir")
            return False
    if atraccion == "Casa del terror":
        if edad < 6:
            print("No puede subir")
            return False
        else:
            return True
    if atraccion == "Carrusel":
        return True
def calcular_precio(atraccion):
    if atraccion == "Montaña rusa":
        return 1500
    if atraccion == "Casa del terror":
        return 1200
    if atraccion == "Carrusel":
        return 800
def registrar_visita():
    nombre = input("Ingrese el nombre del visitante: ")
    edad = int(input("Ingrese la edad del visitante: "))
    atr1 = False
    atr2 = False
    atr3 = False
    contador = 0
    precio_total = 0
    while contador < 3:
        atraccion = mostrar_atracciones()
        if puede_subir(edad, atraccion):
            precio = calcular_precio(atraccion)
            precio_total += precio
            if atraccion == "Montaña rusa":
                atr1 = True
            elif atraccion == "Casa del terror":
                atr2 = True
            elif atraccion == "Carrusel":
                atr3 = True
        contador += 1
    if contador == 3:
        descuento = precio_total * 0.10
        precio_total -= descuento
    resumen = f"Nombre:{nombre}\nEdad:{edad}\n"
    if atr1:
        resumen += "Sube a la montaña rusa\n"
    if atr2:
        resumen += "Sube a la casa del terror\n"
    if atr3:
        resumen += "Sube al carrusel\n"
    resumen += f"Total a pagar: ${int(precio_total)}"
    return resumen
def mostrar_resumen(resumen):
    print(resumen)
