# se salta ese paso, pero vuelve a entrar en el bucle.

# esto sería que pinte los impares, porque cuando encuentre un impar. Me lo salto y no continúo
for i in range(1,1000):
    if i % 2 == 0:
        continue
    print (i)

# esto sería que pinte los pares, porque cuando encuentre un par. Me lo salto y no continúo

for i in range(1,1000):
    if i % 2 != 0:
        continue
    print (i)

