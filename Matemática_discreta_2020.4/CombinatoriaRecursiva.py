# Exercicio 22 completo da lista de atividades da semana 6
# BSI-PLE 2020.4
# 14/02/21
# Graziela Maria

def soma(n, k):
    r = (n - k) / (k + 1)
    return r


n = int(input("Digíte um valor n:"))
k = int(input("Digite um valor para k:"))  # é responsavel pelas k chamadas recursivas.
c = 1


if k == 0:  # caso base
    print("\nO valor de Cn,k é: 1")
else:
    for k in range(0, k):
        sum = soma(n, k)
        c = sum * c

    print("\nO valor para Cn,k é: {}".format(c))
