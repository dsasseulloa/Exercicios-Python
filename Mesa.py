class Mesa:
    # def __init__(self,jogador,cartas):
    #     self.jogador = Jogador
    #     self.cartas = Cartas(['a'])

    def Jogo(self,cartas,jogador,cartas_embaralhadas):

        continuar_jogo = True
        contador = 0
        cartas_escolhidas = jogador.cartas_viradas

        while continuar_jogo:
            cartas_do_jogador = jogador.virar_carta(cartas_embaralhadas)
            print(f"Você pegou a carta {cartas_do_jogador} ")

            cartas_do_jogador_int = (cartas.conversao_cartas(cartas_do_jogador[0]))
            cartas_escolhidas.append(int(cartas_do_jogador_int))

            if cartas_escolhidas[0] == 'A':
                contador += 11
            else:
                contador += int(cartas_do_jogador_int)
            print(f'Cartas na mão: {cartas_escolhidas}')
            print(f"A soma da suas cartas vale: {contador}")


            if contador == 21:
                print("Parabens, você ganhou o jogo")
                break
            if contador > 21:
                print("Voce perdeu o jogo")
                break
            else:
                input("pegar mais uma carta? y/n ")



# ['♦','♣','♠','♥']