#Crear una función buscar_mayor que reciba tres números y devuelva los tres números 
# ordenados de mayor a menor. Luego, el programa debe pedir los números y mostrar los números ordenados.
def buscar_mayor(num1, num2, num3):
    return sorted([num1, num2, num3], reverse=True)
input1 = int(input("Ingrese el primer número: "))
input2 = int(input("Ingrese el segundo número: "))
input3 = int(input("Ingrese el tercer número: "))
resultado = buscar_mayor(input1, input2, input3)
print("Números ordenados de mayor a menor:", resultado)