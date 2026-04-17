nota = float(input('Dime tu nota'))

if nota >= 0 and nota < 5:
    print('Suspenso')
    print('Otra cosa')

if nota >= 5 and nota <=10:
    print('Aprobado')

"""
    Pide por input el importe de una compra
    Si el importe es mayor que 100 muestra el mensaje:
        "Aplicamos un 10% de descuento"
    Y además, mostramos el precio con el descuento aplicado
"""

# 1. Pedir el importe al usuario
precio = float(input("Importe de la compra: "))

# 2. Comprobar la condición (Condicional Simple)
if precio > 100:
    print("Aplicamos un 10% de descuento")
    
    # Cálculo del descuento y precio final
    precio_con_descuento = precio * 0.90
    print (f'Precio original: {precio}€. Precio Descuento: {precio_con_descuento}€')
    
