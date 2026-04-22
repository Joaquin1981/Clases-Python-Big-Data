 # una función puede tener dos tipos de parámetros
    # parametros Obligatorios
    # parámetros Optativos


# Obligatorios

numero_1 = 3
numero_2 = 23

def sumar(nmero_A, numero_B):
    resultado = numero_1 + numero_2
    print(resultado)

sumar(23,8)
sumar(numero_1,numero_2)

# tiene que dar: 
    # 31
    # 26

# función de potencia 3 elevado a 4 (10 elevado 6) y que valga para cualquier número

def potencia(base,exponente):
    resultado = base ** exponente
    print(resultado)

potencia(3,4)
potencia(10,6)

# Optativos: los parámetros Obligatorios tienen que ir primero y después los Optativos. En el momento que incluya un Optativo todos los siguientes parámetros tienen que ser Optativos.

def potencia(base,exponente = 3):
    resultado = base ** exponente
    print(resultado)

potencia(3)
potencia(10,6)

# Sacar la Media de tres números cualesquiera
# Pista: la suma de los tes números dividido entre la cantidad
 
def media(numero_1, numero_2,numero_3):
    suma = numero_1 + numero_2 + numero_3
    media = suma / 3
    print(media)

media(2,3,5)

# función
def media(numero_1, numero_2,numero_3):
    suma = numero_1 + numero_2 + numero_3
    media = suma / 3

# procedimiento
    print(media)

