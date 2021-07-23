# Exercicio 4 da lista de atividades da semana 7
# BSI-PLE 2020.4
# 25/02/21
# Probabilidade de aniversariar em dias distintos

def fatorial(num, fat):
    for n in range(1, num+1):
        fat *= n
    return fat


num = int(input("Insira o valor de n:"))
k = int(input("Insira o valor de k:"))
fat = 1
sub = num-k

n = fatorial(num, fat)
j = fatorial(sub, fat)
i = num**k
C = 1 - (n/(i*j))
print(C)
