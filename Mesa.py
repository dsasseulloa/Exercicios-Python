from Jogador import Jogador
class Mesa:
    # def __init__(self,jogador,cartas):
    #     self.jogador = Jogador
    #     self.cartas = Cartas(['a'])

    def quantidade_jogadores(self):
        lista_jogadores=[]
        num_jogadores=int(input("quantos jogadores na mesa:"))
        for i in range((num_jogadores)):
            print(i)
            jogador = Jogador
            jogador.nome=input("Nome do jogador")
            lista_jogadores.append(jogador.nome)
        return lista_jogadores

    def Pegar_carta(self,jogador):
        pass


    def Jogo(self,lista_jogadores):
        for i in lista_jogadores:
            print(i)
            continuar_jogo = True
            while continuar_jogo = True

    # def Jogo(self,cartas,jogador,cartas_embaralhadas):
    #
    #     continuar_jogo = True
    #     contador = 0
    #     cartas_escolhidas = jogador.cartas_viradas
    #
    #     while continuar_jogo:
    #         continua = True
    #         cartas_do_jogador = jogador.virar_carta(cartas_embaralhadas)
    #         print(f"Você pegou a carta {cartas_do_jogador} ")
    #
    #         cartas_do_jogador_int = (cartas.conversao_cartas(cartas_do_jogador[0]))
    #         cartas_escolhidas.append(int(cartas_do_jogador_int))
    #
    #         if cartas_escolhidas[0] == 'A':
    #             contador += 11
    #         else:
    #             contador += int(cartas_do_jogador_int)
    #         print(f'Cartas na mão: {cartas_escolhidas}')
    #         print(f"A soma da suas cartas vale: {contador}")
    #
    #
    #         if contador == 21:
    #             print("Parabens, você ganhou o jogo")
    #             break
    #         if contador > 21:
    #             print("Voce perdeu o jogo")
    #             break
    #         else:
    #             x=input("Pegar mais uma carta? y/n ")
    #             if x == 'y' or x=="Y":
    #                 continue
    #             if x =='n' or x=="N":
    #                 print("n")
    #                 break
    #             else:
    #                 while x != 'y' or x != 'n':
    #                     print('insira y ou n')
    #                     x = input("Pegar mais uma carta? y/n ")
    #                     if x == 'y' or x=="Y":
    #                         break
    #                     if x =='n' or x=="N":
    #                         continuar_jogo = False
    #                         print("perdeu")
    #                         break
    #
