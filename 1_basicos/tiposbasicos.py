nombre_alumno = "Joaquín Navarro"
print(nombre_alumno) # Joaquín Navarro
print (type(nombre_alumno))

nombre_alumno = 21
print(nombre_alumno)
print(type(nombre_alumno))

# Tipos Básicos en Python

# Numéricos

edad = 44
grados = -27
precio = 1299.35

# Booleano

estado = True
estado = False

# Cadena de caracteres - String

nombre = "Joaquín"
apellidos = 'Navarro'
mensaje = 'El niño dijo: "Qué pasa"'
print (mensaje)

# Joaquín Navarro:44
nombre_completo = nombre + "" + apellidos + ";" + str(edad)
print(nombre_completo)

nombre_completo2 = f'{nombre} {apellidos}: {edad}'
print(nombre_completo2)

texto_largo = """
Selecciona una opción
[1] Sopa
[2] Puré de calabaza 
[3] Gazpacho

"""
opcion = input(texto_largo)
print(f'La opción es {opcion}')
