from random import randint


def cocktail(lista):
    houvetroca = True

    while houvetroca:
        houvetroca = False
        for i in range(len(lista) - 1):
            if lista[i] > lista[i + 1]:
                temp = lista[i]
                lista[i] = lista[i + 1]
                lista[i + 1] = temp
                houvetroca = True

        for i in range(len(lista) - 1, 0, -1):
            if lista[i] < lista[i - 1]:
                temp = lista[i]
                lista[i] = lista[i - 1]
                lista[i - 1] = temp
                houvetroca = True


lista = []

for i in range(10):
    lista.append(randint(0, 20))

cocktail(lista)
print(lista)
