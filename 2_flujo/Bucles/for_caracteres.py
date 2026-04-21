texto = "Joaquín Navarro"

# un string es una cadena de texto,es decir, una cadena de caracteres

# cuantos caracteres tiene un texto.
print (len(texto)) # cantidad de caracteres
print(texto[0]) # para obtener el primer caracter, J
print(texto[10]) # el espacio es un caracter, por lo tanto la letra que imprime es A

texto = "Joaquín Navarro"

# range(len(texto)) genera números del 0 al 14
for i in range(len(texto)):
    # Imprimimos el caracter que está en la posición i
    print(texto[i])

# cualquier letra a mayúscula upper() y cualquier letra en minúscula lower()
# imprimir solo las mayúsculas

for i in range(len(texto)):
    if texto[i] == texto[i].upper():
        print(texto[i])

# imprimir sólo las minúsculas
for i in range(len(texto)):
    if texto[i] == texto[i].lower():
        print(texto[i])

# pedir un texto por pantalla de cualquier longitud y quiero que pida una vocal
# contar cuantas vocales tiene el texto.

# paso 1: Pedir el texto por pantalla. Lo pasamos todo a minúsculas, que también podría ser upper, todo en mayúsulas
texto = input('Dame una frese maravillosa:').lower()
# paso 2: Pedir una vocal
vocal = input('Dame una vocal:').lower()

# paso 3: pintar todos los caracteres del texto
cantidad = len(texto)
for i in range(cantidad):
    print(texto[i])

# paso4: imprimir sólo la vocal pedida
for i in range(cantidad):
    if texto[i] == vocal:
        print(texto[i])

# paso 5: contar las vocales. crear una variable que incremente en 1 cada vez que encuentre mí vocal
numero_vocales = 0
for i in range(cantidad):
    if texto[i] == vocal:
        numero_vocales = numero_vocales + 1
        # numero_vocales += 1





# 1. Entrada de datos de cualquier longitud. Pasamos el texto 
frase = input("Escribe un texto: ")
vocal_buscada = input("¿Qué vocal quieres contar?: ").lower()

# 2. El Acumulador (Fundamental en Ingeniería del Datos)
contador = 0

# 3. El Bucle de Procesamiento
for i in range(len(frase)):
    # Pasamos la letra actual a minúscula para compararla bien con la vocal
    if frase[i].lower() == vocal_buscada:
        contador = contador + 1  # También puedes poner contador += 1

# 4. Resultado Final
print(f"La vocal '{vocal_buscada}' aparece {contador} veces en el texto.")