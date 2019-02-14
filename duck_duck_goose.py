import sys
lista_nombres = ["pedro", "lechuga", "juan", "fernando"]
num_elegido = int(sys.argv[1])

def duck_duck_goose(lista_nombres,num_elegido):
    while num_elegido > len(lista_nombres):
        num_elegido = num_elegido - 4
    jugador_elegido = lista_nombres[num_elegido - 1]
    return jugador_elegido

print(duck_duck_goose(lista_nombres,num_elegido))
