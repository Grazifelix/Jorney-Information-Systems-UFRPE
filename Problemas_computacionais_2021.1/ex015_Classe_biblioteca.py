# classes Biblioteca e Livro:
# - A Biblioteca contem uma lista de livros disponiveis e uma lista de livros alugados
# - A biblioteca possui um metodo para alugar um livro. Caso o livro jah esteja alugado a pessoa nao poderah alugar este livro.
# - A biblioteca possui um metodo para devolver o livro.
# - A biblioteca possui um metodo que devolve o nome do livro mais alugado.
#ENTRADA: 3 234 Fortaleza Digital Dan Brown 423 Calculo 1 Stwart 156 Fisica Tipler
# Graziela Maria
# 07/07/21

class Livro:
    codigo = None
    nome = None
    autor = None
    __qtdeAlugueis = 0

    def __init__(self, codigo, nome, autor):
        self.codigo = codigo
        self.nome = nome
        self.autor = autor
        
    def __cmp__(self, livro):
        return __cmp__(self.codigo, livro.codigo)
        
    def incrementaAluguel(self):
        self.__qtdeAlugueis += 1
    def getQtdeAlugueis(self):
        return self.__qtdeAlugueis

class Biblioteca:
    alugados = []
    disponiveis = []

    def inserir(self, livro):
        self.disponiveis.append(livro)

    def alugar(self, livro):
        ok = True
        mensagem = None
        if livro in self.disponiveis:
            for i in self.disponiveis:
                if i == livro:
                    i.incrementaAluguel()
                    self.alugados.append(i)
                    self.disponiveis.remove(i)
                    break
        elif livro in self.alugados:
            ok = False
            mensagem = "O livro ja esta alugado, infelizmente voce nao podera alugar"
        else:
            ok = False
            mensagem = "O livro nao existe"
        return (ok, mensagem)

    def devolver(self, codLivro):
        ok = True
        mensagem = None
        for livro in self.alugados:
            if livro.codigo == codLivro:
                self.disponiveis.append(livro)
                self.alugados.remove(livro)
                break
        else:
            ok = False
            mensagem = "O livro nao esta alugado"
        return (ok, mensagem)

    def livroMaisAlugado(self):
        ok = True
        mensagem = None
        maior = 0
        nome = None
        for livro in self.disponiveis:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        for livro in self.alugados:
            if livro.getQtdeAlugueis() > maior:
                maior = livro.getQtdeAlugueis()
                nome = livro.nome
        if maior == 0:
            ok = False
            mensagem = "Nenhum livro foi alugado ainda"
        else:
            mensagem = "O livro mais alugado e: %s (%d alugueis)"%(nome, maior)
            return (ok, mensagem)

    def livrosOrdenadosPeloNome(self):
        #Biblioteca.disponiveis = sorted(Biblioteca.disponiveis, key=lambda livro: livro.nome)
        # ORDENANDO LISTA DE DISPONÍVEIS
        elemento = self.disponiveis
        troca = True
        while troca:
            troca = False
            for i in range(len(elemento) - 1):
                if elemento[i].nome > elemento[i + 1].nome:
                    elemento[i], elemento[i + 1] = elemento[i + 1], elemento[i]

                    troca = True

        # ORDENANDO LISTA DE ALUGADOS
        elemento2 = self.alugados
        troca = True
        while troca:
            troca = False
            for i in range(len(elemento2) - 1):
                if elemento2[i].nome > elemento2[i + 1].nome:
                    elemento2[i], elemento2[i + 1] = elemento2[i + 1], elemento2[i]

                    troca = True
        '''
        disponiveis = []
        for livro in self.disponiveis:
            # print(livro.codigo, livro.nome, livro.autor)
            disponiveis.append([livro.codigo, livro.nome, livro.autor])
        alugados = []
        for livro in self.alugados:
            alugados.append([livro.codigo, livro.nome, livro.autor])
            '''
        return (self.disponiveis, self.alugados)

# input split com tabulação. EX: 2	Ola mundo	333
lista = input().split('\t')
#print(lista)

# Programa principal INSERIR LIVRO:
b = Biblioteca()
qtd_livros = lista[0]
j = 1
for i in range(int(qtd_livros)):
    l = Livro(int(lista[j]), lista[j+1], lista[j+2])
    b.inserir(l)
    j = j + 3
b.alugar(l)
#print(*b.livrosOrdenadosPeloNome())

# Merge Sort

ordenados = b.livrosOrdenadosPeloNome()
print(ordenados)
i = 0
j = 0
resultado = []
listaEsquerda = ordenados[0]
listaDireita = ordenados[1]
while i < len(listaEsquerda) and j < len(listaDireita):
    if listaEsquerda[i][1] <= listaDireita[j][1]:
        resultado.append(listaEsquerda[i])
        i += 1
    else:
        resultado.append(listaDireita[j])
        j += 1
resultado += listaEsquerda[i:]
resultado += listaDireita[j:]

saida = []
for i in range(len(resultado)):
    saida.append(resultado[i][0])
print(*saida)



'''
#TESTE
#ordenação alfabética simples - BubbleSort
n = ["c", 'a', 'b']
for i in range(len(n)):
    if i == len(n)-1:
        print(n)
    elif n[i] > n[i+1]:
        n[i], n[i+1] = n[i+1], n[i]

#rdenação alfabética  - BubbleSort
n = ['ca', 'aa', 'bc', 'cb']
troca = True
while troca:
    troca = False
    for i in range(len(n)-1):
        if n[i] > n[i + 1]:
            n[i], n[i + 1] = n[i + 1], n[i]
            troca = True
print(n)

for i in range(len(elemento)):
    if i == len(elemento) - 1:
        print(elemento)
    elif elemento[i].nome > elemento[i + 1].nome:
        '''
'''
l = Livro(123, "Calculo 1", "Stwart")
l2 = Livro(22, "Ciencia", "Luana")
b = Biblioteca()
b.inserir(l)
b.inserir(l2)
print(Biblioteca.disponiveis[0].nome) # printar objeto especifico
'''
'''
l = Livro(123, "Calculo 1", "Stwart")
l2 = Livro(22, "Ciencia", "Luana")
b = Biblioteca()
b.inserir(l)
b.inserir(l2)

'''


