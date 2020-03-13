import random


class Cartas:
    def __init__(self,cartas):
        self.cartas=cartas

    def embaralhar_cartas(self,cartas):
        num_cartas=13
        cartas_embaralhadas=[]
        for i in range(0,num_cartas):
            a = random.choice(cartas)
            cartas.remove(a)
            cartas_embaralhadas.append(a)
        return cartas_embaralhadas

    def conversao_cartas(self,carta):
        if carta == 'Q' or carta == 'J' or carta == 'K' or carta== 'A':
            return 10
        return carta
