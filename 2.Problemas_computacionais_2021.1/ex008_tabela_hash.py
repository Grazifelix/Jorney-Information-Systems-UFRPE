# 22/06/21
# GRAZIELA MARIA
# Tabelas Hash – endereçamento aberto usando containers
# ENTRADA: 11 3 7 8 10 21 31 32 9 21 31 9 9 10 13 32 54

#Função inserir elementos nos containers da tabela hash
def hash_insert(list, elem, qtde_conteiners, tam_containers):
    conteiner = elem % qtde_conteiners
    posicao = conteiner*tam_containers
    for i in range(tam_containers):
        if list[posicao+i] == None:
            list[posicao+i] = elem
            break
        elif i == tam_containers-1:
            list = hash_insert_overflow(list, elem, qtde_conteiners, tam_containers)
    return list

#Função inserir elementos no overflow
def hash_insert_overflow(list, elem, qtde_conteiners, tam_containers):
    posicao = (qtde_conteiners*tam_containers)
    for i in range(posicao, len(list)):
        if list[i] == None:
            list[i] = elem
            break
    return list

#Função de busca de elementos e contagem de comparações
def search_tab_hash(list, elem, qtde_conteiners, tam_containers):
    conteiner = elem % qtde_conteiners
    posicao = conteiner * tam_containers
    contador = 0
    for i in range(tam_containers):
        contador += 1
        if list[posicao+i] == None:
            break
        else:
            if list[posicao+i] == elem:
                break
            elif i == tam_containers-1:
                contador = search_overflow(list, elem, qtde_conteiners, tam_containers, contador)
    return contador

#Função de busca no overflow
def search_overflow(list, elem, qtde_conteiners, tam_containers, contador):
    for i in range((qtde_conteiners * tam_containers), len(list)):
        contador += 1
        if list[i] == None:
            break
        else:
            if list[i] == elem:
                break
    return contador


# ENTRADA E CRIAÇÃO DA TABELA HASH VAZIA
entrada = list(map(int,input().split()))
qtde_containers = entrada[0]
tam_containers = entrada[1]
qtde_insersoes = entrada[3]
tabela_hash = [None]*((qtde_containers*tam_containers)+entrada[2])


# CHAMANDO FUNÇÃO HASH INSERT PARA OS ELEMENTOS QUE SERÃO ADICIONADOS
for i in range(4, qtde_insersoes+4):
    tabela_hash = hash_insert(tabela_hash, entrada[i], qtde_containers, tam_containers)
print(tabela_hash)

# PROCURANDO ELEMENTOS E RETORNANDO NUMERO DE COMPARAÇÕES
cont = []
for i in range((4 + qtde_insersoes), len(entrada)):
    cont.append(search_tab_hash(tabela_hash, entrada[i], qtde_containers, tam_containers))
print(*cont)



