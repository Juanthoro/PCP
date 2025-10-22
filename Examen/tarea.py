import sys, statistics

def mostrar_menu():
    print("\n=== MENÚ DE TEMPERATURAS ===")
    print("1. Insertar nueva temperatura")
    print("2. Mostrar temperatura media")
    print("3. Mostrar temperatura más alta")
    print("4. Mostrar temperatura más baja")
    print("5. Mostrar todas las temperaturas")
    print("6. Salir")
    print("=============================")

def calcular_media(temperaturas):
    if temperaturas:
        return sum(temperaturas) / len(temperaturas)
    else:
        return None
