def buscar_valor(lista, valor):
    for i in range(len(lista)):
        if lista[i] == valor:
            return i
    return -1
        
print(buscar_valor([1, 2, 3, 4, 5], 3))  # Debería devolver 2
print(buscar_valor([1, 2, 3, 4, 5], 6))  # Debería devolver -1