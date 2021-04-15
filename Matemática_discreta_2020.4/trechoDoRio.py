# Exercicio 9 da lista de atividades da semana 7
# BSI-PLE 2020.4
# 27/02/21

import numpy as np

def functionOne(x):
    y=4+x**2
    return y
def functionTwo(x):
    y=1+x**2
    return y

a = 4
b = 8
N = 100000
n = 0

x = a+(b-a)*np.random.uniform(size=N)
max_y=max([functionOne(x[i]) for i in range(N)])
min_y=min([functionTwo(x[i]) for i in range(N)])
y = max_y*np.random.uniform(size=N)

for i in range(N):
    if y[i] < functionOne(x[i]):
      if y[i] > functionTwo(x[i]):
        n+=1

Result = max_y*(b-a)*(n/N)
print("O resultado é {}".format(Result))
