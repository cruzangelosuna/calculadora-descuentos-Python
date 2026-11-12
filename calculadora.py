
print("CALCULADORA DE DESCUENTOS")

precio = float(input("Ingresa el precio del producto: "))
descuento = float(input("Ingresa el porcentaje de descuento: "))

total = precio - (precio * descuento / 100)

print("El precio final es:", total)
