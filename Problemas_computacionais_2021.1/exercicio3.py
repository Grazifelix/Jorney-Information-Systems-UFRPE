#UFRPE - PLE 2020.4
#PROBLEMA DAS PEÇAS PERDIDAS
#26/12/20

n = int(input())
pecas = list(map(int,input().split()))

def somaP(p):
    somaP = 0
    for i in p:
        somaP = somaP + i
    return somaP

somaPecas = somaP(pecas)
soma = n*(n+1)//2

pecaPerdida = soma - somaPecas
print(pecaPerdida)
