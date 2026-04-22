# Me permite mator rango de cambios ( mayor versatilidad) en el desarrollo del bucle. Con el bucle white puedo cambiar los elementos de dentro

# for i in range (1,10):
#    print(i)

j = 1
while j <=10:
    print(j)
    j = j + 1
    print(j)
    if j% 2 != 0:
        break

else:
    print('he terminado el bucle')


