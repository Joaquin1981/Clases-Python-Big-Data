# todos los bucles tienes una secuencia de escape que se lanza  siempre que el bucle se completa. el Else termina cuando termina el bucle

for i in range(1,20):
    if i % 5 == 0:
        continue
    print(i)

else:
    print('el bucle a terminado')

for i in range(1,20):
    if i % 5 == 0:
        break
    print(i)

else:
    print('el bucle a terminado')