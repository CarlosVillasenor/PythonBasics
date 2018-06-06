# -*- coding: utf-8 -*-
# This comment tell  Python that this file has utf-8 characters code

# This is common comment

"""
Esto es un comentarío o  Here-doc, permite ademas ser un String si lo asignas a una variable
"""
# Cadenas de carracteres (strings)

nombre = 'Carlos'
apellido = 'Castillo' # Usar comillas simples es lo ideal en Python

# We joining two strings we need to manually create an space with ' '
nombre_completo = nombre + ' ' + apellido
print(nombre_completo)

# len function counts the number of characters in Strings
print(len(nombre)) #length
# upper transforms an String tu upperCase, lower does the oposite
print(nombre.upper())
# replace finds and replaces letters in a String
print(nombre.replace('o','x'))

# String formating
# we can use %s to call a variable or a function an add it to a string
mensaje_de_saludo = 'Hola soy %s' % nombre_completo
print(mensaje_de_saludo)

nombre_dado = input('Dime tu nombre: ')
print('Tu nombre tiene %s caracteres' %len(nombre_dado) )

#Statements dont have value by itself
#Expresion return values