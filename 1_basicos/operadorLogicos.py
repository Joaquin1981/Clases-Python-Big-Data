# and, or, not
precio = float(input('Dime un precio: '))
marca = input('Dime una marca: ')

resultado = precio > 100 and marca == "apple"
print(resultado)

# número par o divisible por 5
# 1. Pedir el número
# 2. Hacer la comprobación

numero = float(input("Introduce un número: "))

es_par = numero % 2 == 0
es_multiplo_de_5 = numero % 5 == 0

resultado = es_par or es_multiplo_de_5
print(resultado)

# negación

esta_activo = True
print(not esta_activo)