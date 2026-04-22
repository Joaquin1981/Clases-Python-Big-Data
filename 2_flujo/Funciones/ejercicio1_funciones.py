# quiero una función que me permita calcular sumas, restas y multiplicaciones de dos números.
    # Encapsulado de Funciones

# sumar()
def sumar(numero_A, numero_B):
    return numero_A + numero_B

# restar()
def restar(numero_A, numero_B):
    return numero_A - numero_B

# multiplicar
def multiplicar(n_A, n_B):
    return n_A * n_B
    

# 
def calcular(n1,n2, operacion):
    resultado = 0
    if operacion == 'sumar':
        resultado = sumar(n1, n2)
    elif operacion == 'restar':
        resultado = restar(n1, n2)
    elif operacion == 'multiplicar':
        resultado = multiplicar(n1, n2)
    else:
        print('operacion no valida')
    print(resultado)

calcular (12,2,'restar')
