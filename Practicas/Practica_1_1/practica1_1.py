# 📝 Práctica 1.1: Fundamentos de Python

# Juan Francisco Vega Redondo VS2DAW

#################################################################################################

## 🔹 Ejercicio 1: Tipos de datos y entrada de usuario

# Pide al usuario su nombre, edad y altura en metros.
nombre = input("Dime tu nombre")
edad = int(input("Dime los años que tienes"))
altura = float(input("Dime tu altura en metros"))

# Muestra un mensaje usando f-string con los datos ingresados.
print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

# Muestra el tipo de dato de cada variable.
print("Nombre: ", type(nombre))
print("Edad: ", type(edad))
print("Altura: ", type(altura))

#################################################################################################

## 🔹 Ejercicio 2: Funciones básicas

# Crea una función saludar(nombre) que reciba un nombre y devuelva un saludo:
def saludar(nombre):
    return f"¡Hola {nombre}!"

# Crea una función calcular_imc(peso, altura) que devuelva el IMC usando la fórmula:
def calcular_imc(peso, altura):
    return peso / (altura ** 2)

# Llama a estas funciones con los datos ingresados en el ejercicio 1 y muestra los resultados.

print(saludar(nombre))
peso = float(input("Dime tu peso en kg"))

imc = calcular_imc(peso, altura)
print(f"Tu IMC es: {imc}")

#######################################################################################################

## 🔹 Ejercicio 3: Parámetros con valores por defecto y \*args

# Crea una función presentar_persona(nombre="Usuario", edad=None, *aficiones) que muestre un mensaje como:
def presentar_persona(nombre="Usuario", edad=None, *aficiones):
    # Construir mensaje
    mensaje = f"{nombre}"
    
    if edad is not None:  # Solo muestra la edad si se proporciona
        mensaje += f" tiene {edad} años"
    
    if aficiones:  # Solo muestra aficiones si se pasan
        mensaje += " y le gusta: " + ", ".join(aficiones)
    
    print(mensaje)


# Prueba la función con diferentes números de aficiones
presentar_persona("Juan",43,"comer","hacer deporte","leer")


#######################################################################################################

## 🔹 Ejercicio 4: Manejo de errores

# Modifica el ejercicio 1 para que la edad y altura se pidan en un bucle que repita hasta que se ingrese un número válido.
# Usa try/except para capturar errores si el usuario escribe algo que no sea un número int o float en cada caso.

# Pedir nombre (no requiere validación numérica)
nombre = input("Dime tu nombre")

# Bucle para pedir la edad (Casteo a entero)
while True:
    try:
        edad = int(input("Dime los años que tienes"))
        break
    except ValueError:
        print("Error: la edad debe ser un número entero.")

# Bucle para pedir la altura (Casteo a decimales)
while True:
    try:
        altura = float(input("Dime tu altura en metros"))
        break
    except ValueError:
        print("Error: la altura debe ser un número decimal.")


print(f"Hola {nombre}, tienes {edad} años y mides {altura} metros.")

#################################################################################################

## 🔹 Ejercicio 5: Librería externa

# pip install emoji

# import emoji

# print(emoji.emojize("¡Bienvenido! :smile:", language="alias"))


# import emoji

# def calcular_imc_con_emoji(peso, altura):
#     imc = peso / (altura ** 2)
#     if imc < 18.5:
#         estado = "Bajo peso " + emoji.emojize(":warning:", language="alias")
#     elif imc < 25:
#         estado = "Normal " + emoji.emojize(":smile:", language="alias")
#     else:
#         estado = "Sobrepeso " + emoji.emojize(":exclamation:", language="alias")
#     return imc, estado



#####################################################################################################

## 🔹 Ejercicio 6: Entorno virtual y requirements

# pip install emoji
# pip freeze > requirements.txt

#######################################################################################################

## 🔹 Ejercicio 7:

# Pide al usuario una lista de números separados por coma, por ejemplo
listanumeros = input("Introduce una lista de números separados por coma: ")

# Convierte la entrada a lista de enteros.
numeros = [int(n) for n in listanumeros.split(",")]

# Calcula y muestra: suma, promedio, máximo y mínimo usando funciones
suma = sum(numeros)
promedio = suma / len(numeros)
maximo = max(numeros)
minimo = min(numeros)

# Usa f-strings para mostrar los resultados con formato:
print(f"La suma es {suma}, el promedio es {promedio}, el máximo {maximo}, el mínimo {minimo}")

#####################################################################################################

## 🔹 Ejercicio 8: Argumentos desde la línea de comandos

# Crea un archivo `main.py` con el siguiente contenido:

#######################################################################################################

## 🔹 Ejercicio 9: Mini-calculadora por línea de comandos

# Vas a crear un programa que funcione como una **mini-calculadora** desde la consola.
# Crea un archivo `calculadora.py` que al ejecutarse acepte 3 argumentos, un número, un operador (+, \*, / o -) y otro número.
# Si el número de argumentos es incorrecto o los argumentos no son del tipo que se espera debe mostrar error y una ayuda de cómo se usa
# Usa emojis en las salidas para que sea más vistoso.

#!/usr/bin/env python3
import sys

def mostrar_ayuda():
    print("📘 Uso: python calculadora.py <número1> <operador> <número2>")
    print("👉 Operadores válidos: +  -  *  /")
    print("🔢 Ejemplo: python calculadora.py 8 * 5")
    sys.exit(1)

def main():
    # Validación de número de argumentos
    if len(sys.argv) != 4:
        print("⚠️ Error: Número de argumentos incorrecto.")
        mostrar_ayuda()

    num1, operador, num2 = sys.argv[1], sys.argv[2], sys.argv[3]

    # Validación de números
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValueError:
        print("❌ Error: No es un número.")
        mostrar_ayuda()

    # Operaciones
    resultado = None
    if operador == "+":
        resultado = num1 + num2
    elif operador == "-":
        resultado = num1 - num2
    elif operador == "*":
        resultado = num1 * num2
    elif operador == "/":
        if num2 == 0:
            print("💥 Error: No se puede dividir entre cero.")
            sys.exit(1)
        resultado = num1 / num2
    else:
        print(f"❌ Error: Operador inválido '{operador}'.")
        mostrar_ayuda()

    print(f"✅ Resultado: {num1} {operador} {num2} = {resultado}")

if __name__ == "__main__":
    main()

#######################################################################################################

