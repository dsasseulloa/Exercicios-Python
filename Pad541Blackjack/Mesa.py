from Jogador import Jogador
from Cartas import Cartas
class Mesa:
    # def __init__(self,jogador,cartas):
    #     self.jogador = Jogador
    #     self.cartas = Cartas(['a'])

    def quantidade_jogadores(self):
        lista_jogadores=[]
        while True:
            try:
                num_jogadores=int(input("quantos jogadores na mesa: "))
                if num_jogadores < 1 or num_jogadores > 7:
                    print("favor digitar um numero entre 1 e 7")
                else:
                    break
            except ValueError:
                print('Favor digitar um numero')

        for i in range((num_jogadores)):
            nome = input(f"Nome do jogador número {i+1}: ")
            jogador = Jogador(nome)
            lista_jogadores.append(jogador)
        croupier=Jogador("Le Croupier")
        lista_jogadores.append(croupier)
        return lista_jogadores

    def pegar_carta(self,jogador,cartas_embaralhadas):
        carta_virada = jogador.virar_carta(cartas_embaralhadas)
        print(f"O jogador {jogador.nome} recebeu a carta {carta_virada} ")
        carta_virada_convertida = Cartas().conversao_cartas(carta_virada)
        if jogador.cartas_viradas == ['A'] and carta_virada=='A':
            jogador.pontos += 11
        else:
            jogador.pontos += int(carta_virada_convertida)
        print("Pontos do jogador :", jogador.pontos)
        print("Cartas na mão: ", jogador.cartas_viradas)


    def Jogo(self,lista_jogadores):
        cartas_embaralhadas=Cartas().embaralhar_cartas()
        jogadores_participando=lista_jogadores.copy()
        rodar_jogo=True
        lista_de_pontos = []
        while rodar_jogo:
            continuar_pegando_carta = True
            if jogadores_participando == []:
                print('O jogou acabou, segue a contagem de pontos:')
                for i in range(len(lista_jogadores)):
                    lista_de_pontos.append(lista_jogadores[i].pontos)
                    print(f'O jogador(a) {lista_jogadores[i].nome} fez {lista_jogadores[i].pontos} pontos')
                rodar_jogo=False
                ganhador = max(lista_de_pontos)
                while ganhador > 21:
                    ganhador=max(lista_de_pontos)
                    if ganhador > 21:
                        ganhador=0
                    else:
                        break
                print(ganhador)
                print("Ganhadores: ")
                for i in range(len(lista_jogadores)):
                    if lista_jogadores[i].pontos == ganhador:
                        print(f'{lista_jogadores[i].nome} com {lista_jogadores[i].pontos} pontos')

            for i in range(0,len(jogadores_participando)):
                jogador = jogadores_participando[i]
                print(f'RODADA DO JOGADOR {jogador.nome}')
                if len(jogador.cartas_viradas) < 2:
                    self.pegar_carta(jogador,cartas_embaralhadas)
                    if jogador.pontos == 21 and jogador.nome == "Le Croupier":
                        print(f'O Croupier fez BLACKJACK e ganhou a mesa')
                        jogadores_participando.pop(i)
                        break
                    elif jogador.pontos == 21:
                        print(f'O Jogador {jogador.nome} fez BLACKJACK')#ganhou 3:2 da sua aposta e saiu da rodada
                        jogadores_participando.pop(i)
                        break
                    break
                else:
                    while continuar_pegando_carta:
                        resposta=input(("Pegar mais uma carta? y/n "))
                        if resposta == 'n' or resposta == 'N' :
                            jogadores_participando.pop(i)
                            print("--------------------------------")
                            continuar_pegando_carta = False
                            break
                        if resposta == 'y' or resposta == 'Y':
                            self.pegar_carta(jogador, cartas_embaralhadas)
                            if jogador.pontos > 21:
                                print("O jogador passou de 21 pontos e perdeu suas apostas")
                                jogadores_participando.pop(i)
                                lista_jogadores.pop(i)
                                continuar_pegando_carta = False
                            elif jogador.pontos == 21:
                                print(
                                    f'O Jogador {jogador.nome} fez BLACKJACK, ganhou 3:2 da sua aposta e saiu da rodada')
                                jogadores_participando.pop(i)
                                continuar_pegando_carta = False
                                break
                            print("--------------------------------")
                        else:
                            print('Porfavor digite "y" ou "n"')
                    break
