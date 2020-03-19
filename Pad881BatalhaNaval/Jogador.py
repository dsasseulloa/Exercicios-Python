from BatalhaNaval import BatalhaNaval
from Navio import Navio
class Jogador(BatalhaNaval):
    def __init__(self):
        self.nome=""
        super().__init__()
        self.navio=super().criar_navio()


    def definir_nome(self,n):
        nome = input(f"Jogador {n}, Qual o seu nome? ")
        self.nome = nome

    def lista_de_jogadores(self):
        lista_jogadores=[]
        for i in range(0, 2):
            jogador = Jogador()
            lista_jogadores.append(jogador)

        return lista_jogadores

    def inicializacao_jogo(self):
        jogador=self.lista_de_jogadores()
        count=1
        for i in range(0, 2):
            jogador[i].definir_nome(count)
            count+=1
            jogador[i].criar_matriz_jogo(jogador[i],jogador[i].lista_matriz)
            jogador[i].criar_matriz_jogo(jogador[i],jogador[i].lista_de_comparacao)
            print(f'{jogador[i].nome}, posicione seus navios: ')
            self.posicionar_navio(jogador[i])
        self.partidas(jogador)
        pass

    def partidas(self,lista_jogadores):
        jogador=lista_jogadores
        jogo_continua=True
        while jogo_continua:
            for i in range(0,2):
                if jogador[i].continuar_jogo_ate_nao_ter_barcos(jogador[i]):
                    jogada_valida=True
                    while jogada_valida:
                        jogada = input(f"{jogador[i].nome} digite uma coordenada para tentar acertar um navio inimigo!: (Exemplo: 5A) ").upper()
                        if jogador[i].percorrer_matriz_de_comparacao(jogada,jogador[i]):
                            jogador[i].chechar_campo_do_outro_jogador(jogada,jogador[i-1])
                            jogada_valida=False
                        else:
                            print("Coordenada inválida")

                else:
                    print(f"O jogo acabou e o ganhador foi o {jogador[i-1].nome}")
                    jogo_continua = False
                    break

    def teste_inicializacao_jogo_com_2_navios(self):
        jogador=self.lista_de_jogadores()
        count=1
        for i in range(0, 2):
            jogador[i].definir_nome(count)
            count+=1
            jogador[i].criar_matriz_jogo(jogador[i],jogador[i].lista_matriz)
            jogador[i].criar_matriz_jogo(jogador[i],jogador[i].lista_de_comparacao)

        print("matriz do ",jogador[0].nome)
        jogador[0].alterar_matriz('1E', 'cima', jogador[0].navio[4])
        jogador[0].alterar_matriz('2E', 'cima', jogador[0].navio[5])
        jogador[0].criar_matriz_asci()
        print("matriz do ",jogador[1].nome)
        jogador[1].alterar_matriz('10E', 'cima', jogador[1].navio[4])
        jogador[1].alterar_matriz('9E', 'cima', jogador[1].navio[5])
        jogador[1].criar_matriz_asci()

        self.partidas(jogador)

        pass