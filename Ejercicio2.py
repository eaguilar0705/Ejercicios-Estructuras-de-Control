"""Escribir un programa que permita emitir la FACTURA correspondiente, a una compra de
un artículo determinado, del que se adquieren una o varias unidades. El IVA a aplicar es de 15%
y si el Sub Total (precio de venta por cantidad), es mayor de 1000, se aplicará un descuento del 12%."""

while True:
    articulo = input("Ingrese el nombre del articulo: ")
    cantidad = int(input("Ingrese la cantidad de unidades: "))
    precio = float(input("Ingrese el precio por unidad: "))
    
    subtotal = cantidad * precio
    iva = subtotal * 0.15
    total = subtotal + iva
    
    if subtotal > 1000:
        total *= 0.88  # Aplicar descuento del 12%
    
    print("\nFACTURA")
    print("Articulo:", articulo)
    print("Cantidad:", cantidad)
    print("Precio unitario:", precio)
    print("Sub total:", subtotal)
    print("IVA:", iva)
    print("Total:", total)
    
    continuar = input("\n¿Desea emitir otra factura? (s/n): ")
    if continuar.lower() != 's':
        break
