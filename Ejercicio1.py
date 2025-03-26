while True:
    vehiculo = input("Ingrese el tipo de vehiculo (o 'salir' para terminar): ")
    if vehiculo == 'salir':
        break

    total = 100

    if vehiculo == "moto" or vehiculo == "carro":
        km = float(input("Ingrese la cantidad de kilometros recorridos: "))
        total = km * 30

    elif vehiculo == "camion":
        km = float(input("Ingrese la cantidad de kilometros recorridos: "))
        toneladas = float(input("Ingrese la cantidad de toneladas del camion: "))
        total = (km * 30) + (toneladas * 25)

    else:
        print("Tipo de vehículo no válido.")
        total = None

    if total is not None:
        print("El importe a pagar es:", total, "córdobas.")