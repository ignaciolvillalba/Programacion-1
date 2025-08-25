estacion = input("Ingrese el nombre de la estación(verano, invierno, otoño, primavera): ")
destino = input("Ingrese el destino (Bariloche, Cataratas, Mar del plata): ")
match estacion:
    case "invierno":
        if destino == "Bariloche":
            print("Se viaja")
        else:
            print("No se viaja")
    case "verano":
        if destino in ["Cataratas", "Mar del plata"]:
            print("Se viaja")
        else:
            print("No se viaja")
    case "otoño":
        print("Se viaja")
    case "primavera":
        if destino == "Bariloche":
            print("No se viaja")
        else:
            print("Se viaja")