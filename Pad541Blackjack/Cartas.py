import random
class Cartas:
    def __init__(self,cartas=['2','3','4','5','6','7','8','9','10','A','J','Q','K']):
        self.cartas=cartas

    def embaralhar_cartas(self):
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
