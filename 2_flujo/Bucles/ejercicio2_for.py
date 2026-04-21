# pintar por pantalla 1000 numeros pero solo los pares.
# Empezando de 1 hasta 1000. No se puede cambiar los valores iniciales.

# paso 1: bucle desde 1 hsata 1000
# paso 2: pintar 1000 números
# paso 3: pintar sólo los pares. Tiene que funcionar para impares también

# números pares
for i in range(1, 1000):
    if i % 2 == 0:
        print(i)

# números impares
for i in range(1, 1000):
    if i % 2 != 0:
        print(i)
