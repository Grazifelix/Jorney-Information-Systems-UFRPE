# 10/05/21
# Graziela Maria
# exemplo entrada: 7 1 2 3 4 5 6 7 5 2 7 9 1
# primeiro numero - comprimento da lista
# numeros ordenados - é a lista que será usada para procurar os numeros.
# numeros embaralhados - numeros para procurar dentro da lista ordenada.
# Saída: Numero de vezes que cada numero da lista de numeros embaralhados é verificado.

def binary_search(n, item, begin=0, end=None, cont=None):
    if cont is None:
        cont = 1
    if end is None:
        end = len(n)-1
    if begin <= end:
        m = (begin + end)//2
        if n[m] == item:
            return cont #,item
        if item < n[m]:
            cont += 1
            return binary_search(n, item, begin, m-1, cont)
        else:
            cont += 1
            return binary_search(n, item, m+1, end, cont)
    return cont-1

n_search = list(map(int, input().split()))

n_length = n_search[0]
list_ordered = []
cont_comparations = []

#print(n_search)
if len(n_search) == 1:
    print("Entrada inválida. Insira uma estrada com mais de um item.")
else:
    n_search.pop(0)
    for i in range(0, n_length):
        list_ordered.append(n_search[0])
        #print(list_ordered)
        n_search.pop(0)

    for item in n_search:
       cont_comparations.append(binary_search(list_ordered, item))
    print(*cont_comparations)


