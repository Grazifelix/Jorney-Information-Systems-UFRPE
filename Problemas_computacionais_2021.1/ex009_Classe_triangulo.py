# 07/07/21
# Graziela Maria
# Calcular perimetro de um triangulo

class Triangulo:
    LadoA = None
    LadoB = None
    LadoC = None

    def __init__(self, LadoA, LadoB, LadoC):
        self.LadoA = LadoA
        self.LadoB = LadoB
        self.LadoC = LadoC

    def calculaPerimetro(self):
        return self.LadoA + self.LadoB + self.LadoC

#t = Triangulo(10, 5, 6)
#print(t.calculaPerimetro())
t = []
for i in range(1, 4):
    t.append(int(input("Insira lado {}: ".format(i))))
t = Triangulo(t[0], t[1], t[2])
print("O perimetro do triangulo é: ", t.calculaPerimetro())