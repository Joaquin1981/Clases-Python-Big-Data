# necesito que pidais varios numeros por pantalla y que los sumeis. El programa termina cuando metemos el número 0:

# con While.
# paso 1: pedir número constantemente
# paso 3: añadir a suma el valor introducido previamente convertido.
# paso 4: pulsando 0 acabamos el ejercicio

suma = 0
while True:
    numero = int(input('Introduce un número'))
    if numero == 0:
        break
    suma += numero

print(suma)

# ahora ponemos la solución más estética

print('#' * 40)
print('EJERCICIO 4 - SUMA ACUMULADA')
print('#' * 40)
print(" ")

suma = 0
while True:
    numero = int(input('Introduce un número'))
    if numero == 0:
        break
    suma += numero

print(suma)