class Jogador:
    def __init__(self,cartas_viradas,nome):
        self.cartas_viradas=cartas_viradas
        self.nome=nome

    def virar_carta(self, cartas_embaralhadas):
        cartas_viradas = []
        pegar_carta = cartas_embaralhadas[0]
        cartas_viradas.append(pegar_carta)
        cartas_embaralhadas.pop(0)
        return cartas_viradas