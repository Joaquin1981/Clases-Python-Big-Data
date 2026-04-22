# Una función tiene dos partes - la una sin la otra no pueden convivir.

# Error. No se puede ejecutar una función antes de la Declaración

despedir()

# parte 1: DECLARACIÓN - DEFINICIÓN

def saludar():
    print('Hola desde una funcion')

def despedir():
    print('Vete a tu casa')

# parte 2: Ejecutamos la funcion

saludar()

despedir()

# por ejemplo:

for i in range (1000):
    saludar()


