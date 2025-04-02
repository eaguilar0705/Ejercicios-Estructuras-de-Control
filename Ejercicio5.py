import math

def calcular_area():
    while True:
        print("=========================")
        print("CÁLCULO DE SUPERFICIES (versión 1.0)")
        print("=========================")
        print("1. Cuadrado      lado*lado")
        print("2. Círculo       pi*radio*radio")
        print("3. Rectángulo    base*altura")
        print("4. Trapecio      (base1+base2)*altura/2")
        print("5. Triángulo     (base*altura)/2")
        print("=========================")

        opcion = input("Seleccione una opción (1-5) o 'salir' para terminar: ").strip()

        if opcion.lower() == 'salir':
            print("Programa terminado.")
            break

        if opcion not in {'1', '2', '3', '4', '5'}:
            print("Opción inválida. Intente de nuevo.")
            continue

        if opcion == '1':  # Cuadrado
            lado = float(input("Ingrese el lado del cuadrado: "))
            area = lado * lado
            print(f"El área del cuadrado es: {area:.2f}")

        elif opcion == '2':  # Círculo
            radio = float(input("Ingrese el radio del círculo: "))
            area = math.pi * radio * radio
            print(f"El área del círculo es: {area:.2f}")

        elif opcion == '3':  # Rectángulo
            base = float(input("Ingrese la base del rectángulo: "))
            altura = float(input("Ingrese la altura del rectángulo: "))
            area = base * altura
            print(f"El área del rectángulo es: {area:.2f}")

        elif opcion == '4':  # Trapecio
            base1 = float(input("Ingrese la base menor del trapecio: "))
            base2 = float(input("Ingrese la base mayor del trapecio: "))
            altura = float(input("Ingrese la altura del trapecio: "))
            area = (base1 + base2) * altura / 2
            print(f"El área del trapecio es: {area:.2f}")

        elif opcion == '5':  # Triángulo
            base = float(input("Ingrese la base del triángulo: "))
            altura = float(input("Ingrese la altura del triángulo: "))
            area = (base * altura) / 2
            print(f"El área del triángulo es: {area:.2f}")

        print("\n¿Desea realizar otro cálculo?")

if __name__ == "__main__":
    calcular_area()