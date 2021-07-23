# 04/05/21

def fatorial(n):
    fat = 1
    for n in range(1, num+1):
        fat = fat * n
    return fat


n = int(input("Insira o fatorial: "))
num = n-1
print("O fatorial de {} é igual a: {}".format(n, fatorial(num)/2))


