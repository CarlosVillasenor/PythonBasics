#-*- coding: utf-8 -*-
# colecciones 

#lista (array)

grupo_back = ['cesar', 'Miguel', 'Toño']

len(grupo_back)

# diccionarios 

persona = {
    'nombre': 'Hector', 
    'apellido': 'Patricio',
    'edad': 28,
    'hobbies': ['leer', 'programar', 'dormir'],
    'tiene_mascotas': True
}
persona['nombre']
print(persona['nombre'])
# how to call a key the correct way
persona.get('estatura')
print(persona.get('estatura'))
# Sending a second parameter we will  give to our get a value in case it does not exist
persona.get('estatura', 1.65)
