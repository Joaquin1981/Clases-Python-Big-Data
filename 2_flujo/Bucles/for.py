for i in range(5):
    print('Hola')
for i in range(100):
    print ('Hola' + str(i))
for i in range(100):
    print (f'Hola + {i}')


# paso 1: Almacenar la cantidad de unidades
# paso 2: Pedir esa cantidad por pantalla
# paso 3: Convertir la unidad en número (debido a que el input da un stream)
# paso 4: Meterla en el For
# paso 5: Ejecutar el script

# paso 1.
cantidad = 100

for i in range(100):
    for i in range(100):


# paso 2.
cantidad = input('Dime una cantidad:')

for i in range(100):
    #print(f'Hola {i}')

# paso 3. 
cantidad = int('Dime una cantidad:')
print( type(cantidad))

for i in range(100):
    #print(f'Hola {i}')

# paso 4.
cantidad = int(input('Dime una cantidad:'))
print( type(cantidad))

for i in range(cantidad):
    print(f'Hola {i}')

# Versión 2. Poder elegir punto de inicio y punto de fin en el Bucle

for i in range(2, 8):
    print(f"Valor: {i}")

# Versión 3: Poder elegir punto inicio el punto y los saltos o cuentas.

for i in range(2, 15, 3):
    print(f'Valor: {i}')

