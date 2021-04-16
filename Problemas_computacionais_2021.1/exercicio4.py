#Graziela Maria
#BSI - FPC I 2021.1
# 15/04/21
# Cálculo de complexidade (até 2 níveis de loops aninhados)

n = input().split()


def AmountLoop(a):
    loop = 0
    for i in range(0, len(a)):
        if a[i] == "FIMLOOP":
            loop += 1
    return loop


fimloop = AmountLoop(n)
complexidade = 0
while True:

    for i in range(0, fimloop):
        if n[i] == "OP":

        if n[i] == "LOOP":
            print(int(n[i+1]))
            print(fimloop)

    break