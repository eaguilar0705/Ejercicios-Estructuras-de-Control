"""Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento del 15% por
la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3 docenas se obsequia una unidad
del producto por cada docena en exceso sobre 3. Diseñe un programa que determine el monto de la compra, el monto del
descuento, el monto a pagar y el número de unidades de obsequio por la compra de cierta cantidad de docenas del producto."""
while True:
    docenas = int(input("Ingrese la cantidad de docenas a comprar: "))
    precio = float(input("Ingrese el precio por docena: "))
    
    unidades = docenas * 12
    subtotal = unidades * precio
    descuento = 0
    obsequio = 0
    
    if docenas > 3:
        descuento = subtotal * 0.15
        obsequio = (docenas - 3) * 12
    else:
        descuento = subtotal * 0.10
    
    total = subtotal - descuento
    
    print("\nCOMPRA")
    print("Unidades:", unidades)
    print("Sub total:", subtotal)
    print("Descuento:", descuento)
    print("Total:", total)
    print("Obsequio:", obsequio)
    
    continuar = input("\n¿Desea realizar otra compra? (s/n): ")
    if continuar.lower() != 's':
        break