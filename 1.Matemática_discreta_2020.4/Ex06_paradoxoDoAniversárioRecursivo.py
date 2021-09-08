'''
def fatorial(num, fat, cont):
    for n in range(1, num+1):
        fat *= cont/365
        cont = cont - 1
    return fat

n = int(input("Insira o numero de aniversariantes:"))
cont = 365
fat = 1
print("A porcentagem de chances de fazerem aniversario em datas distintas é: {:.1f}%".format(fatorial(n, fat, cont)*100))

'''

def fatorial(num, fat, cont):
    for n in range(1, num+1):
        fat *= cont
        cont = cont - 1
    return fat

n = int(input("Insira o numero de aniversariantes:"))
cont = 365
fat = 1
result = 1 - fatorial(n, fat, cont)/(365**n)
print("A porcentagem de chances de fazerem aniversário no mesmo dia é: {:.1f}%".format(result*100))
