# Graziela Maria
# BSI - FPC I 2021.1
# 21/04/21
# Cálculo de complexidade (até 2 níveis de loops aninhados)
# Exemplo de entrada: INICIO LOOP 10 OP 3 OP 2 FIMLOOP FIM


n = input().split()

def soma_elementos(lista):
    total = 0
    for i in lista:
       total = total + i
    return total

loopex = 0
soma = []
result = 0

if n[1] == "LOOP":
    loopex = int(n[2])
    loop = 0
    op = 0
    for i in range(len(n[2]), len(n)):
        if n[i] == "LOOP":
            loop = int(n[i + 1])
        elif n[i] == "OP":
            op = op + int(n[i + 1])
    if loop == 0:
        mult = 1 * op
    else:
        mult = loop * op
    soma.append(mult)
    somado = soma_elementos(soma)
    result = loopex * somado
    print(result)








