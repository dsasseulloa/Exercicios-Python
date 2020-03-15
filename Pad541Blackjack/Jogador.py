class Jogador:
    def __init__(self,nome):
        self.cartas_viradas=[]
        self.nome=nome
        self.pontos=0

    def virar_carta(self, cartas_embaralhadas):
        pegar_carta = cartas_embaralhadas[0]
        self.cartas_viradas.append(pegar_carta)
        cartas_embaralhadas.pop(0)
        return pegar_carta

