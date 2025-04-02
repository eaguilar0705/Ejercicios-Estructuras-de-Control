"""Diseñe un programa que lea un número de tres cifras y determine si es igual al revés del número."""

while True:
    numero = input("Ingrese un número de tres cifras: ")

    if len(numero) != 3 or not numero.isdigit():
        print("El número debe tener exactamente tres cifras.")
        continue
    
    numero_reves = numero[::-1]
    
    if numero == numero_reves:
        print("El número es igual al revés del número.")
    else:
        print("El número no es igual al revés del número.")
    
    continuar = input("\n¿Desea ingresar otro número? (s/n): ")
    if continuar.lower() != 's':
        break