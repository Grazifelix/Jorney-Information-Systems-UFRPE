#Sequencia de fibonacci
#19/12/20

'''
def fib(n):
    print("Calculando fibonacci  {}.".format(n))
    if n<=1:
        return n
    else:
        a = (n-3)
        b = (n-2)
        return a+b
while True:
     n = int(input("Numero:"))
     if n:
        print(fib(n))
     else:
     break
'''

#sequencia de fibonacci recursiva
#status: NÃO CONCLUÍDA

def fib(n):
   # print("Calculando fibonacci  {}.".format(n))
    if n<=1:
        return n
    else:
        return fib(n-2) + fib(n-1)

while True:
     n = int(input("Numero:"))
     if n:
        print(fib(n))
     else:
        ""
     break
