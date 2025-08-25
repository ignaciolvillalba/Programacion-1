#Crear una función convertir_minutos(minutos) que reciba una cantidad de minutos y devuelva cuántas horas y minutos sobran
def convertir_minutos(minutos):
    horas = minutos // 60
    minutos_sobran = minutos % 60
    return horas, minutos_sobran