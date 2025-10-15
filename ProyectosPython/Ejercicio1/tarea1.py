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

###########################################################################################################
# Tabla de multiplicar
# Aqui el error seria no castear a int en la entrada del valor, lo que provocaria que pusiera el valor
# de la variable las veces que hemos puesto=> 3, 33, 333, 3333, etc.
variabletabla = int(input("Dime la tabla de multiplicar que quieres :"))

for i in range (11):
    resultado = variabletabla*i
    print(f"{variabletabla} x {i} = {resultado}")
###########################################################################################################


