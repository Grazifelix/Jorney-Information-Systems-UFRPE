#Inicio: 24/06/21 - Fim:

import random
from itertools import permutations



#INICIO ALGORITMO

# LEITURA DE MATRIZ A PARTIR DE UM ARQUIVO .TXT

arquivo = open("Casos testes/caso5(CUIDADO).txt", "r")
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


#ALGORITMO GENÉTICO
def algoritmoGenetico(pontos, tamanhoPopulacao, taxaDeReproducao, probabilidadeMutacao, criterioParada):
    # CRIANDO POPULAÇÃO INICIAL A PARTIR DO TAMANHO DEFINIDO
    populacao = []
    if len(pontos) < 5 and tamanhoPopulacao < 25:
        permutacoes = permutations(pontos)
        for i in list(permutacoes):
            populacao.append(i)
    else:
        cont = 0
        while cont < tamanhoPopulacao:
            pt = pontos * 1
            individuo = []
            for i in range(0, len(pontos)):
                id = random.randint(0, len(pt) - 1)
                individuo.append(pt[id])
                pt.remove(pt[id])
            populacao.append(individuo)
            cont += 1
        print(populacao)

    # CALCULANDO FITNESS DA POPULAÇÃO INICIAL

    fitnessPopulacao = []
    fitnessTotal = 0 #soma do fitness total de todos os individuos
    for i in range(0, tamanhoPopulacao):
        fitnessPopulacao.append(fitness(populacao[i]))
        fitnessTotal = fitnessTotal + fitnessPopulacao[i][0]
    fitnessPopulacao = sorted(fitnessPopulacao)
    print(fitnessPopulacao)
    print(fitnessTotal)


    # CALCULANDO PROBABILIDADES PARA O METODO DA ROLETA
    piso = 0
    for i in range(0, tamanhoPopulacao):
        fitnessPopulacao[i].append(round(fitnessTotal/fitnessPopulacao[i][0], 2))
        fitnessPopulacao[i].append(round(piso + fitnessPopulacao[i][2], 2))
        piso = round(piso + fitnessPopulacao[i][2] + 0.01, 2)

    # RETORNANDO OS PARES DE PAIS PARA CROSSOVER
    pais = roleta(fitnessPopulacao, taxaDeReproducao)
    novaPopulacao = crossover(pais, probabilidadeMutacao)
    populacao = sorted(fitnessPopulacao + novaPopulacao)

    # AJUSTE POPULACIONAL
    populacao = ajustePopulacional(populacao, tamanhoPopulacao)

    return populacao

#calculo do fitness(Aptidão)
def fitness(individuo):
    # CALCULANDO DISTANCIAS TOTAIS ENTRE CIDADES DE CADA INDIVIDUO
    fitnessIndividuo = []
    soma_dist = 0
    pt = str(individuo[0])
    soma_dist = soma_dist + geoTaxi(dic_pontos['R'][0], dic_pontos['R'][1], dic_pontos[pt][0], dic_pontos[pt][1])
    for j in range(1, len(individuo)):
        if j == len(individuo) - 1:
            pt = str(individuo[j])
            soma_dist = soma_dist + geoTaxi(dic_pontos[pt][0], dic_pontos[pt][1], dic_pontos['R'][0],
                                                dic_pontos['R'][1])
        else:
            ptA = str(individuo[j])
            ptB = str(individuo[j + 1])
            soma_dist = soma_dist + geoTaxi(dic_pontos[ptA][0], dic_pontos[ptA][1], dic_pontos[ptB][0],
                                                dic_pontos[ptB][1])


    fitnessIndividuo.append(soma_dist)
    fitnessIndividuo.append(individuo)

    return fitnessIndividuo


#calculo da geometria do taxi
def geoTaxi(x1, y1, x2, y2):
    D = abs((x2-x1))+abs((y2-y1))
    return D


#método da roleta
def roleta(populacao, taxaDeReproducao):
    pop = populacao*1
    cont = 0
    pais = []
    taxa = int(len(populacao) * ((taxaDeReproducao/2) / 100)) #Como são pares de pais 100% é o mesmo que a metade dos individuos, ou seja vou precisar rodar o while 50 vezes para fazer pares de todos os meus individuos
    print("A taxa é : ", taxa)
    while cont < taxa:
        pai = []
        for i in range(0, 2):
            limite = round(pop[int(len(pop)/2)][3], 2) #dividi por dois para o limite do random ser o valor do individuo do meio - pegar o valor medio
            roletaPonteiro = round(random.uniform(pop[0][3]-1, limite), 2)
            #print(round(roletaPonteiro, 2))
            for j in range(0, len(pop)-1):
                if j == 0:
                    limiteInferior = 0
                    limiteSuperior = pop[j][3]
                    if roletaPonteiro > limiteInferior and roletaPonteiro <= limiteSuperior:
                        #print(pop[j])
                        pai.append(pop[j])
                        pop.remove(pop[j])
                        break
                else:
                    limiteInferior = pop[(j-1)][3]
                    limiteSuperior = pop[j][3]
                    if roletaPonteiro > limiteInferior and roletaPonteiro <= limiteSuperior:
                        #print(pop[j])
                        pai.append(pop[j])
                        pop.remove(pop[j])
                        break
        pais.append(pai)
        cont += 1

    return pais

#CROSSOVER

def crossover(pais, probabilidaDeMutacao):
    novaPopulacao = []
    filho1 = ''
    filho2 = ''
    pai1 = ''
    pai2 = ''
    pontoCorte = random.randint(1, len(pais[0][0][1])-1)
    for i in range(0, len(pais)-1):
        pai1 = pais[i][0][1]
        pai2 = pais[i][1][1]
        filho1 = pai1[0:pontoCorte]+pai2[pontoCorte:len(pai2)]
        filho2 = pai2[0:pontoCorte]+pai1[pontoCorte:len(pai1)]
        filho1 = mutacao(filho1, probabilidaDeMutacao)
        filho2 = mutacao(filho2, probabilidaDeMutacao)
        orgarnizarFilho(pai1, filho1)
        orgarnizarFilho(pai1, filho2)
        novaPopulacao.append(filho1)
        novaPopulacao.append(filho2)
        #print(pontoCorte, pai1, pai2, filho1, filho2)

    for i in range(0, len(novaPopulacao)):
        novaPopulacao[i] = fitness(novaPopulacao[i])
    novaPopulacao = sorted(novaPopulacao)
    print(novaPopulacao)

    return novaPopulacao

# Função para organizar os filhos e tirar as repetições de letras
def orgarnizarFilho(pai, filho):
    # verificando as letras repetidas e as letras faltando
    letrasRepetidas = [k for k in pai if filho.count(k) > 1]
    letraFaltando = list(set(pai).difference(set(filho)))
    ids = []
    #print("Repetidas:", letrasRepetidas)
    #print("Faltando:", letraFaltando)

    # Verificando os indices das letras repetidas
    if letrasRepetidas == []: #se letras repetidas for igual a zero, retorna filho.
        return filho
    else:
        #senão, compara os itens da lista faltando com os itens do filho e verifica os duplicados.
        for i in range(0, len(letrasRepetidas)):
            c = 0
            for x in range(0, len(filho)):
                if filho[x] == letrasRepetidas[i]:
                    c += 1 #contador para não pegar o primeiro item da lista
                    if c > 1:
                        ids.append(x)
        #print(ids)

    for j in range(0, len(ids)):
        filho[ids[j]] = letraFaltando[j]
    return filho



# função de mutação
def mutacao(filho, taxaDeMutacao):
    taxa = random.uniform(0.0, 1.0)
    if taxa < taxaDeMutacao:
        id = random.randint(0, len(filho)-1)
        id2 = random.randint(0, len(filho)-1)
        aux = filho[id]
        filho[id] = filho[id2]
        filho[id2] = aux

    return filho

# Ajustando população para 
def ajustePopulacional(populacao, tamanhoPopulacao):

    while len(populacao) > tamanhoPopulacao:
        tam = len(populacao)
        individuo1 = random.randint(0, tam-1)
        individuo2 = random.randint(0, tam-1)
        if individuo1 != individuo2:
            if populacao[individuo1][0] < populacao[individuo2][0]:
                populacao.remove(populacao[individuo2])
            else:
                populacao.remove(populacao[individuo1])


    return populacao


# CALCULANDO PERMUTAÇÕES
#tamanhoPopulacao = int(input("Insira o tamanho da população inicial: "))
tamanhoPopulacao = 200
taxaDeReproducao = 100
probabilidadeMutacao = 0.1
criterioParada = 3

ag = algoritmoGenetico(pontos, tamanhoPopulacao, taxaDeReproducao, probabilidadeMutacao, criterioParada)
#print(ag)

for i in range(0, len(ag)):
    print(i, ag[i])





