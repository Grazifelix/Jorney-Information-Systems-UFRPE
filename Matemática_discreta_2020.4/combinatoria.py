#Exercicio 22 da lista de atividades da semana 6
#BSI-PLE 2020.4
#14/02/21

def fatorial(num, fat):
    for n in range(1, num+1):
        fat *= n
    return fat


num = int(input("Insira o valor de n:"))
k = int(input("Insira o valor de k:"))
fat = 1
sub = num-k

n = fatorial(num, fat)
i = fatorial(k, fat)
j = fatorial(sub, fat)
C = n/(i*j)
print(n, C)


