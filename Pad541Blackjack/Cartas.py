import random
class Cartas:
    def __init__(self):
        self.cartas=self.criar_baralho()

    def criar_baralho(self):
        naipes=['♥','♦','♣','♠']
        cartas=['2','3','4','5','6','7','8','9','10','A','J','Q','K']
        baralho=[]
        for i in cartas:
            for j in naipes:
                baralho.append(i + j)
        return baralho

    def pegar_numero_do_baralho(self):
        baralho=self.criar_baralho()
        carta=random.choice(baralho)
        return carta[0]

    def embaralhar_cartas(self)->list:
        num_cartas=13
        cartas_embaralhadas=[]
        for i in range(0,num_cartas):
            a = random.choice(self.cartas)
            self.cartas.remove(a)
            cartas_embaralhadas.append(a)
        return cartas_embaralhadas

    def conversao_cartas(self,carta):
        if carta == 'Q' or carta == 'J' or carta == 'K' or carta== 'A':
            return 10
        return carta
