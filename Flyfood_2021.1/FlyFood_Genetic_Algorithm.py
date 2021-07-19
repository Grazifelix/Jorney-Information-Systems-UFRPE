# Inicio: 24/06/21 - Fim: 04/07/21
# GRAZIELA MARIA
# RESOLUÇÃO DO PROBLEMA DO CAIXEIRO VIAJANTE UTILIZANDO UM ALGORITMO GENÉTICO

import random

# PARAMETROS DO ALGORITMO GENÉTICO
tamanhoPopulacao = 10
taxaDeReproducao = 60
probabilidadeMutacao = 0.5
criterioParada = 80


# LEITURA DE MATRIZ A PARTIR DE UM ARQUIVO .TXT
arquivo = open("Casos testes/caso2.txt", "r")
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
    # CALCULANDO FITNESS DA POPULAÇÃO INICIAL
    populacao = sorted(fitness(populacao))
    for i in range(tamanhoPopulacao):
        print("Geração: {} | {}".format("Inicial", populacao[i]))

    # CALCULANDO FITNESS DAS POPULAÇÃO SEGUINTES
    geracao = 1
    for k in range(criterioParada): # laço que se refere ao numero de iterações
        fitnessTotal = 0 # soma do fitness total de todos os individuos
        for i in range(0, tamanhoPopulacao):
            fitnessTotal = fitnessTotal + populacao[i][0]
        populacao = sorted(populacao)
        # print(fitnessTotal)


        # CALCULANDO PROBABILIDADES PARA O METODO DA ROLETA
        piso = 0
        for i in range(0, tamanhoPopulacao):
            populacao[i].append(round(fitnessTotal/populacao[i][0], 2))
            populacao[i].append(round(piso + populacao[i][2], 2))
            piso = round(piso + populacao[i][2] + 0.01, 2)

        # RETORNANDO OS PARES DE PAIS PARA CROSSOVER
        pais = roleta(populacao, taxaDeReproducao)
        novaPopulacao = crossover(pais, probabilidadeMutacao)
        populacao = sorted(populacao + novaPopulacao)

        # AJUSTE POPULACIONAL
        populacao = ajustePopulacional(populacao, tamanhoPopulacao)

        # PRINTANDO POPULAÇÕES

        for i in range(tamanhoPopulacao):
            print("Geração: {} | {}".format(geracao, populacao[i]))

        geracao += 1

    return populacao


# CALCULO DO FITNESS(Aptidão)
def fitness(populacao):
    fitnessPopulacao = []
    for i in range(len(populacao)):
        fitnessIndividuo = []
        soma_dist = 0
        pt = str(populacao[i][0])
        soma_dist = soma_dist + geoTaxi(dic_pontos['R'][0], dic_pontos['R'][1], dic_pontos[pt][0], dic_pontos[pt][1])
        for j in range(len(populacao[i])):
            if j == len(populacao[i]) - 1:
                pt = str(populacao[i][j])
                soma_dist = soma_dist + geoTaxi(dic_pontos[pt][0], dic_pontos[pt][1], dic_pontos['R'][0],
                                                    dic_pontos['R'][1])
            else:
                ptA = str(populacao[i][j])
                ptB = str(populacao[i][j + 1])
                soma_dist = soma_dist + geoTaxi(dic_pontos[ptA][0], dic_pontos[ptA][1], dic_pontos[ptB][0],
                                                    dic_pontos[ptB][1])

        fitnessIndividuo.append(soma_dist)
        fitnessIndividuo.append(populacao[i])
        fitnessPopulacao.append(fitnessIndividuo)

    return fitnessPopulacao


# CALCULO DA GEOMETRIA DO TAXI
def geoTaxi(x1, y1, x2, y2):
    D = abs((x2-x1))+abs((y2-y1))
    return D


# METÓDO DA ROLETA
def roleta(populacao, taxaDeReproducao):
    pop = populacao*1
    cont = 0
    pais = []
    taxa = int(len(populacao) * ((taxaDeReproducao/2) / 100)) # Como são pares de pais 100% é o mesmo que a metade dos individuos, ou seja vou precisar rodar o while 50 vezes para fazer pares de todos os meus individuos
    #print("A taxa é : ", taxa)
    while cont < taxa:
        pai = []
        for i in range(0, 2):
            limite = round(pop[int(len(pop)/2)][3], 2) # dividi por dois para o limite do random ser o valor do individuo do meio - pegar o valor medio
            roletaPonteiro = round(random.uniform(pop[0][3]-1, limite), 2)
            for j in range(0, len(pop)-1):
                if j == 0:
                    limiteInferior = 0
                    limiteSuperior = pop[j][3]
                    if roletaPonteiro > limiteInferior and roletaPonteiro <= limiteSuperior:
                        pai.append(pop[j])
                        pop.remove(pop[j])
                        break
                else:
                    limiteInferior = pop[(j-1)][3]
                    limiteSuperior = pop[j][3]
                    if roletaPonteiro > limiteInferior and roletaPonteiro <= limiteSuperior:
                        pai.append(pop[j])
                        pop.remove(pop[j])
                        break
        pais.append(pai)
        cont += 1
    return pais


# CROSSOVER
def crossover(pais, probabilidaDeMutacao):
    novaPopulacao = []
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
    novaPopulacao = sorted(fitness(novaPopulacao))
    #print(novaPopulacao)

    return novaPopulacao


# MUTAÇÃO
def mutacao(filho, taxaDeMutacao):
    taxa = random.uniform(0.0, 1.0)
    if taxa < taxaDeMutacao:
        id = random.randint(0, len(filho)-1)
        id2 = random.randint(0, len(filho)-1)
        filho[id], filho[id2] = filho[id2], filho[id]
    
    return filho


# REMOVENDO REPETIÇÕES DE LETRAS
def orgarnizarFilho(pai, filho):
    # verificando as letras repetidas e as letras faltando
    letrasRepetidas = [k for k in pai if filho.count(k) > 1]
    letraFaltando = list(set(pai).difference(set(filho)))
    ids = []

    # Verificando os indices das letras repetidas
    if letrasRepetidas == []:
        return filho
    else:
        for i in range(0, len(letrasRepetidas)):
            c = 0
            for x in range(0, len(filho)):
                if filho[x] == letrasRepetidas[i]:
                    c += 1  # contador para não pegar o primeiro item da lista
                    if c > 1:
                        ids.append(x)

    for j in range(0, len(ids)):
        filho[ids[j]] = letraFaltando[j]
    return filho


# AJUSTE POPULACIONAL
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


# IMPRIMINDO MELHOR RESULTADO
ag = algoritmoGenetico(pontos, tamanhoPopulacao, taxaDeReproducao, probabilidadeMutacao, criterioParada)
print("Melhor solução encontrada: {} | {}".format(ag[0][0], ag[0][1]))

