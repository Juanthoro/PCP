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
