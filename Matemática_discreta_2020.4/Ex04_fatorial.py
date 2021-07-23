
def fatorial(num):
    fat = 1
    for n in range(1, num+1):
        fat *= n
    return fat


num = int(input("Insira o valor de n:"))
print("O fatorial de {} é: {}".format(num, fatorial(num)))