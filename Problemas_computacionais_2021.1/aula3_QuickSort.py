# 07/07/21
# Entrada: (sequencias numericas) EX: 10 2 6 8 45 6 3

def quicksort(lista):
    if len(lista) <= 1:
        return lista
    menor, igual, maior = [], [], []
    pivot = lista[0]
    for x in lista:
        if x < pivot:
            menor.append(x)
        elif x == pivot:
            igual.append(x)
        else:
            maior.append(x)
    return quicksort(menor) + igual + quicksort(maior)


lista = list(map(int, input("Insira a lista: ").split()))
print(quicksort(lista))
