
""""    
    Cálculo del precio a pagar en un aparcamiento
    - Pedir el número de horas que ha estado aparcado (número decimales permitidos)
    - Pedir si tiene tarjeta residente o no ("s" o "n")
    - Pedir el tipo de vehículo ("moto", "coche" o "furgoneta")
    - Validamos los datos

    - Cálculo el precio dependiendo de las horas:
        - Primera hora: 2€
        - De 1 a 3 horas: 1.5€/h
        - Más de 3 horas: 1€/h
"""

# 1. Usa tu snippet 'infloat' aquí para las horas

horas = float(input("Dime cuantas horas has permanecido en el parking:"))

residente = input("Tienes tarjeta de residente[s/n] ?").lower() 
vehiculo = input("Tipo de vehículo [coche/moto/furgoneta]").lower()

# 3. Lógica de tramos (Estilo Técnico)
if horas <= 0:
    print('Las horas deben ser un valor positivo')
# elif residente != "s" and residente != "n":
elif residente not in ('s', 'n'):
    print('Responde s o n para la tarjeta de residente')
elif vehiculo not in ('moto','coche','furgoneta'):
    print ('Tipo de vehículo no válido')
else:
    #Todo correcto - Hacemos el cálculo
    if horas <=1:
        precio = 2
    elif horas<=3:
        precio = 2 + (horas - 1)*1.5
    else:
        # Primera hora (2€) + Siguientes dos horas (1.5€) + Resto de horas
        precio = 2 + (2*1.5) + (horas - 3)
        print(f'Has estado {horas} horas. Precio a pagar: {precio}€')
    

# Cáculo multiplicador x vehículo

"""
    - Multiplicador de precio dependiendo del vehículo:
        moto x 0.7, coche x 1, furgoneta x 1.5

    - Aplica 20% descuento sobre el precio si erees residente

    FORMATO:
    --- TICKET DE APARCAMIENTO ---
    Horas: 2.5 | Vehículo: coche | Residente: sí
    Precio base: 3.75 €
    Descuento residente: -0.75 €
    TOTAL: 3.00 €
"""
elif vehiculo =='furgoneta':
multiplicador= 1.5
total = precio * multiplicador

#Descuento residente
descuento = total * 0.2 if residente == 's' else 0
total -= descuento

print(f"""
       --- TICKET DE APARCAMIENTO ---
    Horas: {horas} 2.5 | Vehículo: {vehiculo} | Residente: {residente}
    Precio base: {precio} €
    Descuento residente: -{round(descuento)} €ç
    TOTAL: {round(total)} €
    """)




