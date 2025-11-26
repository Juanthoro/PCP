import barcos

#############################################
if __name__== "main":
    main()
#############################################

def main():
    oceano = []
    for i in range(10):
        fila = []
        for j in range(10):
            fila.append(0)
        oceano.append(fila)


    while True:
        barcos.mostrar_menu()
        option = input("Elige una opción (1-2): ")

        if option == "1":
            barcos.recibir_barcos()

        elif option == "2":
            print("Salir del programa")
            break

        else:
            print("Error. El valor introducido no es válido")




#############################################
if __name__ == "__main__":
    main()
#############################################