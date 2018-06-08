#-*- coding: utf-8 -*-

# Funciones
# Conjunto de código que corre bajo demanda

def calcular_promedio(datos):
    suma = 0
    for dato in datos:
        suma += dato
    promedio = suma / len(datos)
    return promedio

print(calcular_promedio([1,2,3]))

def calcular_iva(precio, tasa_iva=1.16, imprimir=False):
    subtotal = precio / tasa_iva
    iva = precio - subtotal
    if imprimir:
        print(iva)
    return iva

print(calcular_iva(100,1.16,True))
# We can send parameters ignoring parameters between if we named them
print(calcular_iva(116, imprimir=True))