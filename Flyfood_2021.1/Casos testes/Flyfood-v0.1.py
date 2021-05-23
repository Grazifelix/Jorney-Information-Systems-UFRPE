#19/05/21
# Pensando em algoritmos genetinos

# import random

# FORMULA RECURSIVA DA GEOMETRIA DO TAXI

def geoTaxi(x1, y1, x2, y2):
    D = abs((x2-x1))+abs((y2-y1))
    return D

# LEITURA DE MATRIZ A PARTIR DE UM ARQUIVO .TXT


arquivo = open("caso1.txt", "r")

matriz = []

linha = arquivo.readline()
while linha != "":
    elementos = linha.split()
    matriz.append(elementos)
    linha = arquivo.readline()

arquivo.close()

# BUSCA NA MATRIZ e ARMAZENAGEM DE PONTOS EM UM DICIONÁRIO


pontos = []
dic_pontos = {}
for i in range(len(matriz)):
    for j in range(len(matriz[0])):
        letra = matriz[i][j]
        if matriz[i][j] == 'R':
            dic_pontos[letra] = (i, j)
        elif matriz[i][j] != '0':
            dic_pontos[letra] = (i, j)
            pontos.append(letra)
pontos = sorted(pontos)

# Verificando a melhor distancia de R até algum ponto
dist_total = 0
caminho = []
soma = 0
pt = pontos[0]
m_dist = geoTaxi(dic_pontos['R'][0], dic_pontos['R'][1], dic_pontos[pt][0], dic_pontos[pt][1])
m_ponto = pontos[0]

for i in range(0, len(pontos)):
    pt = str(pontos[i])
    dist = geoTaxi(dic_pontos['R'][0], dic_pontos['R'][1], dic_pontos[pt][0], dic_pontos[pt][1])
    if dist < m_dist:
        m_dist = dist
        m_ponto = pt
    print("R -->", pt, dist, m_ponto)
caminho.append(m_ponto)
dist_total = dist_total + m_dist
print(m_dist, m_ponto, dist_total)


# VERIFICANDO O MELHOR PONTO APARTIR DO PONTO ANTERIOR - DIVIDINDO A QUANTIDADE DE PONTOS A SER TESTADOS AO MEIO
list_inicio = int(len(pontos)/2)
print(list_inicio, pt)
m_pontoII = m_ponto


list_inicioII = int((list_inicio + len(pontos))//2)
if list_inicioII == len(pontos)-1:
    m_dist3 = geoTaxi(dic_pontos[m_pontoII][0], dic_pontos[m_pontoII][1], dic_pontos[pt][0], dic_pontos[pt][1])
pt = str(pontos[list_inicioII+1])
print(list_inicioII)

m_ponto3 = m_pontoII
m_dist3 = geoTaxi(dic_pontos[m_pontoII][0], dic_pontos[m_pontoII][1], dic_pontos[pt][0], dic_pontos[pt][1])
for i in range(list_inicioII, len(pontos)):
    pt3 = str(pontos[i])
    dist = geoTaxi(dic_pontos[m_pontoII][0], dic_pontos[m_pontoII][1], dic_pontos[pt3][0], dic_pontos[pt3][1])
    if dist < m_dist3:
        m_dist3 = dist
        m_ponto3 = pt
    print("R -->", pt, dist, m_ponto3)
caminho.append(m_ponto3)
dist_total = dist_total + m_dist3
print(m_dist3, m_ponto3)

dist_final = geoTaxi(dic_pontos[m_ponto3][0], dic_pontos[m_ponto3][1], dic_pontos[pt][0], dic_pontos[pt][1])
print(dist_total+dist_final, caminho)


'''
# SEGUNDA TENTATIVA

# VERIFICANDO O MELHOR PONTO APARTIR DO PONTO ANTERIOR - DIVIDINDO A QUANTIDADE DE PONTOS A SER TESTADOS AO MEIO
list_inicio = int(len(pontos)/2)
pt = pontos[random.randint(list_inicio, len(pontos))]
print(list_inicio, pt)
dist = geoTaxi(dic_pontos[m_ponto][0], dic_pontos[m_ponto][1], dic_pontos[pt][0], dic_pontos[pt][1])
dist_total = dist_total + dist
caminho.append(pt)
m_ponto2 = pt





list_inicio2 = int((list_inicio + len(pontos))//2)
if list_inicio2 == len(pontos)-1:
    # PROBLEMA: Se o list_inicio2 for igual a quantidade de elementos, então da "error out of range"
    pt2 = pontos[random.randint(list_inicio2, len(pontos))]
    print(list_inicio2, pt2)
    dist = geoTaxi(dic_pontos[m_ponto2][0], dic_pontos[m_ponto2][1], dic_pontos[pt2][0], dic_pontos[pt2][1])
    dist_total = dist_total + dist
    caminho.append(pt2)
    m_ponto3 = pt2

'''
