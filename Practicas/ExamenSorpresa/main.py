# Programa de gestión de temperaturas
# Implementa un programa que lea y almacene en un array una serie de temperaturas que irá
# introduciendo el usuario y ofrezca un menú con la posibilidad de insertar nuevas temperaturas
# y calcule la temperatura media, la más alta y la más baja. El programa parará sólo mediante
# una opción del menú.

import tarea

if __name__== "main":
    main()


def main():
    temperaturas = []

    while True:
        tarea.mostrar_menu()
        option = input("Elige una opción (1-6): ")

        if option == "1":
            try:
                temperatura = float(input("Introduce una temperatura: "))
                temperaturas.append(temperatura)
                print("Temperatura añadida")
            except ValueError:
                print("Introduce un número válido.")

        elif option == "2":
            media = tarea.calcular_media(temperaturas)
            if media is not None:
                print(f"Temperatura media: {media:.2f}°C")
            else:
                print("No hay temperaturas guardadas.")

        elif option == "3":
            if temperaturas:
                print(f"Temperatura máxima: {max(temperaturas)}°C")
            else:
                print("No hay temperaturas guardadas.")

        elif option == "4":
            if temperaturas:
                print(f"Temperatura mínima: {min(temperaturas)}°C")
            else:
                print("No hay temperaturas guardadas.")

        elif option == "5":
            if temperaturas:
                print("Lista de temperaturas:", ", ".join(f"{t}°C" for t in temperaturas))
            else:
                print("No hay temperaturas guardadas.")

        elif option == "6":
            print("Salir del programa")
            break

        else:
            print("Error")


if __name__ == "__main__":
    main()
