#Aluna: Graziela Maria
#Data: 10/12/20
#EXERCICIO 1 - CALCULADORA IMPROVISADA

def sucessor(a):
    return a + 1


def soma(a, b):
    for i in range(b):
        a = sucessor(a)
    return a


def multiplicacao(a, b):
    c = 0
    for i in range(b):
        c = soma(c, a)
    return c


def exponenciacao(a, b):
    c = 1
    for i in range(b):
        c = multiplicacao(c, a)
    return c


print('Adicione as entradas:')
while True:
    ent = input()
    if ent:
        ent = ent.split()
        if ent[0] == "Suc":
            print('\nSucessor:', sucessor(int(ent[1])))
        elif ent[0] == "Soma":
            print('\nSoma:', soma(int(ent[1]), int(ent[2])))
        elif ent[0] == "Mult":
            print('\nMultiplicação:', multiplicacao(int(ent[1]), int(ent[2])))
        elif ent[0] == "Exp":
            print('\nExponenciação:', exponenciacao(int(ent[1]), int(ent[2])))
        else:
            print('Esta operação não é permitida.')
    else:
        break
