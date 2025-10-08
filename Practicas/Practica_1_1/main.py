import sys

def main():
    # sys.argv es una lista con los argumentos de la línea de comandos
    # El primer elemento (posición 0) es siempre el nombre del archivo
    print("Argumentos recibidos:", sys.argv)

    # Si hay argumentos adicionales, los mostramos
    if len(sys.argv) > 1:
        nombre = sys.argv[1]
        edad = sys.argv[2]
        print(f"Hola, {nombre} {edad} 👋")
    else:
        print("No se proporcionó ningún argumento")

if __name__ == "__main__":
    main()

    