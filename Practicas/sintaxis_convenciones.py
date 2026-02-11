"""
En este primer programa vamos a practicar la sintaxis basica de python
"""

# Esta orden imprime cualquier texto dentro del parentesis en pantalla
print("Hola Mundo")

# Tipos de datos y variables
edad = 25 # Número entero
precio = 19.99 # Número decimal
nombre = "Python" # Cadena de texto
activo = True # Booleana
ventas = None # Ausencia de valor

print(type(edad)) # Dará int porque es un entero
print(type(precio)) # Dará float porque es un decimal
print(type(nombre)) # Dará str porque es un string
print(type(activo)) # Dará bool porque es un booleano
print(type(ventas)) # Dará NoneType porque es ausencia de valor(el null de java)

# Colecciones #
# Listas
lista1 = [1,2,3,4]
print(lista1)
print(lista1[1]) # Dará el 2 porque empieza en 0

# Tuplas (Estas son listas que no se pueden cambiar)
tupla1 = (10, 20, 30, 40)
print(tupla1)

# Diccionarios
diccionario1 = {
    "nombre":"Paquito",
    "apellido":"Chocolatero",
    "usuario":"chocopaquito",
    "contraseña":"1234"
    }
print(diccionario1["nombre"])

# Conjuntos (No repite elementos)
conjunto1 = {10, 20, 30, 40}
conjunto2 = {1, 2, 3, "hola", "adios"}
conjunto3 = {1, 2, 3, 3, 3}
print(conjunto1)
print(conjunto2)
print(conjunto3)


# Conversion a tipos diferentes #
int("10")       # 10 (toma una cadena y devuelve un número entero)
str(20)         # "20" (toma un número entero y devuelve una cadena)
float("3.14")   # 3.14 (toma una cadena y devuelve un número decimal)

print(int("10"))

# Ejemplos de conversion de datos/ Casteo de Java
numero1 = 0
numero2 = 0

numero1 = input("Introduce un número:")
numero2 = input("Introduce un número:")
print(int(numero1) + int(numero2))


# Condicionales #
edad = 0
edad = int(input("Introduce tu edad:"))

if edad > 18:
    print("Eres mayor de edad")
elif edad == 18:
    print("Tienes justo 18")
else:
    print("Eres menor de edad")


# match estado_web:
#         case 400:
#             return "Bad request"
#         case 401 | 403:
#             return "Not allowed"
#         case 404:
#             return "Not found"
#         case _:
#             return "Something's wrong with the internet"
     
words = ['gato', 'ventana', 'perro']
for w in words:
    print(w)

for i in range(5):
    print(i)


for elemento in lista1:
    print(elemento)


contador = 0
while contador < 5:
    print(contador)
    contador += 1

for i in range(10):
    if i == 5:
        break  # sale del bucle
    if i % 2 == 0:
        continue  # salta al siguiente ciclo
    print(i)

class MiClaseVacia:
    pass  #no hace nada, se usa como marcador de posición


# Excepciones

try:
    # Código que puede lanzar una excepción
    resultado = 10 / 0
except:
    # Código a ejecutar si se produce una excepción
    print("Se produjo una excepción.")


try:
    # Código que puede lanzar una excepción
    resultado = 10 / 0
except ZeroDivisionError:
    # Código a ejecutar si se produce una excepción del tipo ZeroDivisionError
    print("No se puede dividir por cero.")
except ValueError:
    # Código a ejecutar si se produce una excepción del tipo ValueError
    print("Valor incorrecto.")
except:
    # Código a ejecutar si se produce cualquier tipo de excepción
    print("Se produjo una excepción.")



try:
    # Código que puede lanzar una excepción
    resultado = 10 / 2
except ZeroDivisionError:
    # Código a ejecutar si se produce una excepción del tipo ZeroDivisionError
    print("No se puede dividir por cero.")
else:
    # Código a ejecutar si no se produce ninguna excepción
    print("La división fue exitosa. El resultado es:", resultado)
finally:
    # Código a ejecutar siempre, independientemente de si se produce una excepción o no
    print("Esta línea se ejecutará siempre.")



# FUNCIONES Y MÓDULOS #
def saludar(nombre):
    return "Hola, {nombre}"

print(saludar("Lucía"))


def sumar(a, b):
  suma = a + b
  return suma   # Devuelve la suma de a y b

total = sumar(5, 3)  # total ahora será 8


import math     #importamos el módulo math completo
print(math.sqrt(16))


from math import sqrt #solo importa la función sqrt
print(sqrt(25))
  

# Módulos #
# Creamos primero el archivo operaciones.py
# main.py

import operaciones

resultado_suma = operaciones.suma(5, 3)
print("Resultado de la suma:", resultado_suma)


# main.py

import operaciones as ops

resultado_suma = ops.suma(5, 3)
print("Resultado de la suma:", resultado_suma)

from operaciones import resta as restar

resultado_resta = restar(10, 4)
print("Resultado de la resta:", resultado_resta)






