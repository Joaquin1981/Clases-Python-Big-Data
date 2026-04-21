# Quiero que pidiendo un número por pantalla (ej: 7)
# saqueis la tabla de pmultiplicar de este número
# 7 x 1 = 7
# 7 x 2 = 14
# 7 x 3 = 21
# 7 x 4 = 28
# 7 x 5 = 35
# 7 x 6 = 42
# 7 x 7 = 49
# 7 x 8 = 56
# 7 x 9 = 63
# 7 x 10 = 70

# paso 1: pedir un numero por pantalla y convertirlo en int
# paso 2: pintar con un print una primera operación la del 7 x 1 = 7 usando la variable
# paso 3: meter la operación dentro de un bucle
# paso 4: desde que numero inicia hasta que numero va
# paso 5: cambiar el contador dentro del print
# paso 6: ejecutar el script

numero = int (input('Dime un numero:'))
#print(type(numero), numero)

for i in range(1,10):
    print(f'{numero} x {i} = {numero * i}')
    

