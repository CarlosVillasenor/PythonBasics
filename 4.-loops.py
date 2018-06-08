# Loops

# Repeticions

grupo = ['Héctor', 'Foco', 'Carlos']

# Iterating in our array

# tuplas are constant, are faster thant arrays
mi_tupla = (1,2)

#Our Loop
i = 0 # Acumulator
for nombre in grupo:
    print("El alumno en posición %s, se llama: %s" % (i,nombre))
    i+= 1

# Factorial
# n! = n * (n - 1)

# 4! = ((4*3) * 2) * 1)
x = 4
result = 1
for n in range(1, x + 1):
    result = result * n
#     print(result)
   
# print(result)

#calculate promedio of an array
edades =[21,35,25,34,28,23]
# el promedio es la suma de los datos dividido en entre el numero de datos

acumulator = 0
for n in edades:
    print(n)
    acumulator += n
print(acumulator/(len(edades)))    
