import sys

"""
###########################################################################################################
# Dados los catetos dar el valor de la hipotenusa
import math

catetoa = float(input("Dame el valor del cateto a"))
catetob = float(input("Dame el valor del cateto b"))
hipotenusa = math.pow(catetoa,2) + math.pow(catetob,2)
print(math.sqrt(hipotenusa))
###########################################################################################################
"""

"""
###########################################################################################################
# Bucle
# La condición de salida debe ponerse lo ultimo para que entre el valor que definimos primero
# si no no entraria.
contador = 5
while contador < 20 :
    contador+=1
    if contador % 2 == 0:
        #contador+=1
        continue
    elif contador == 15:
        print(f"Llegamos al 15")
        break
    print(f"El valor de contador es {contador}")
###########################################################################################################
"""
"""
###########################################################################################################
# Tabla de multiplicar
# Aqui el error seria no castear a int en la entrada del valor, lo que provocaria que pusiera el valor
# de la variable las veces que hemos puesto=> 3, 33, 333, 3333, etc.
# variabletabla = int(input("Dime la tabla de multiplicar que quieres :"))

#for i in range (11):
#    resultado = variabletabla*i
#    print(f"{variabletabla} x {i} = {resultado}")
###########################################################################################################
"""

global num_usuario

def pintar_tablas(variabletabla):
    for i in range (1,11):
        resultado = variabletabla*i
        print(f"{variabletabla} x {i} = {resultado}")


def pedir_numero():

    global num_usuario

    while num_usuario < 1 or num_usuario > 10:

        if num_usuario > 1 or num_usuario < 10:
            print("Los valores válidos son del 1 al 10")

        try:
            num_usuario = int(input("¿Qué tabla de multiplicar quieres?"))

        except ValueError:
            print("Solo valores del 1 al 10")

        except:
            print("Se ha producido un error")


def ejecutar_con_argumento():
    # argv es el listado de parametros que hemos pasado por consola
    if len(sys.argv) < 1 and len(sys.argv) > 1:
        print("el programa solo recibe un argumento")
    else:
        pintar_tablas(int(sys.argv[0]))