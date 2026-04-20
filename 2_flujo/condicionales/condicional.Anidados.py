inserted. Possible variables are:
// $1, $2 for tab stops, $0 for the final cursos position, and $ {1:label}, ${2:another}


{
	"Input mas Float": {
		"prefix": "infloat",
		"body": [
			"${1:variable} = float(input(\"Introduce ${2:valor}: \"))",
			"print(f\"El valor de ${1:variable} es: {${1:variable}}\")"
		],
		"description": "Pide un numero decimal y lo imprime"
	},
	"Condicional Par": {
		"prefix": "espar",
		"body": [
			"if ${1:numero} % 2 == 0:",
			"\tprint(f\"El {${1:numero}} es par\")",
			"else:",
			"\tprint(f\"El {${1:numero}} es impar\")"
		],
		"description": "Crea un if/else para numeros pares"
	}
}

//ejemplo

nota = float(input('dime tu nota'))

if nota >= 5 :
    print ( "estas apobado")
else :
    print (" estas suspenso")
    
    nota = float(input('dime tu nota: '))
if nota >= 5 and nota <= 10:
    print("Estas aprobado")
elif nota >= 0 and nota < 5:
    print("Estás Suspenso")
else:
    print("Nota no valida")


if nota >= 0 and nota < 5:
    print("Estás Suspenso")
elif nota >= 5  and nota < 6:
    print("Suficiente")
elif nota >= 6 and nota < 7:
    print("Bien")
elif nota >= 7 and nota < 9:
    print("Notable")
elif nota >= 9 and nota < 10:
    print("Sobresaliente")