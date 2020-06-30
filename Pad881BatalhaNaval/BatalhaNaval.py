from Navio import Navio
class BatalhaNaval:
    def __init__(self):
        self.lista_matriz=[]
        self.lista_siglas = ['P', 'E', 'C', 'D', 'S','X']
        self.lista_de_comparacao=[]

    def criar_matriz_jogo(self,jogador,matriz):
        tam_tabuleiro = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', ]
        linhas_tabuleiro = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

        for i in range(len(linhas_tabuleiro)):
            lista_colunas = []
            for j in range(len(linhas_tabuleiro)):
                lista_colunas.append(tam_tabuleiro[j] + linhas_tabuleiro[i])
            matriz.append(lista_colunas)
        return matriz

    def mostrar_matriz(self):
        for i in self.lista_matriz:
            print(i)
        return ""

    def mostrar_matriz_comparacao(self):
        for i in self.lista_de_comparacao:
            print(i)
        return ""

    def criar_matriz_asci(self):
        lista_copia=self.lista_matriz.copy()
        lista_ascii=[]
        for i in range(10):
            lista_colunas = []
            for j in range(10):
                if lista_copia[i][j] not in self.lista_siglas:
                    lista_colunas.append("▓")
                else:
                    lista_colunas.append(lista_copia[i][j])
            lista_ascii.append(lista_colunas)
        linhas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        print("    1    2    3    4    5    6    7    8    9    10")
        tabuleiro=[]
        for i in lista_ascii:
            tabuleiro.append(i)
        for colunas in range(10):
            print(linhas[colunas],tabuleiro[colunas])
        return ""


    def criar_matriz_ascii_escondendo_navios(self):
        linhas = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
        lista_copia=self.lista_matriz.copy()
        lista_ascii=[]
        for i in range(10):
            lista_colunas = []
            for j in range(10):
                if lista_copia[i][j] != 'X':
                    lista_colunas.append("▓")
                else:
                    lista_colunas.append(lista_copia[i][j])
            lista_ascii.append(lista_colunas)
        print("    1    2    3    4    5    6    7    8    9    10")
        tabuleiro = []
        for i in lista_ascii:
            tabuleiro.append(i)
        for colunas in range(10):
            print(linhas[colunas], tabuleiro[colunas])
        return ""

    def lista_posicoes_matriz(self):
        lista_posicoes=[]
        for j in range(len(self.lista_de_comparacao)):
            for i in self.lista_matriz[j]:
                lista_posicoes.append(i)
            return lista_posicoes

    def lista_posicoes_matriz_com_posicoes_alteradas(self):
        lista_posicoes_alteradas=[]
        for j in range(len(self.lista_matriz)):
            for i in self.lista_matriz[j]:
                lista_posicoes_alteradas.append(i)
        return lista_posicoes_alteradas

    def percorrer_matriz(self,obj):
        for j in range(len(self.lista_matriz)):
            for i in self.lista_matriz[j]:
                if obj not in self.lista_siglas and obj == i:
                    return True

    def percorrer_matriz_de_comparacao(self,obj,jogador):
        for j in range(len(jogador.lista_de_comparacao)):
            for i in jogador.lista_de_comparacao[j]:
                if obj in i:
                    return True


    def alterar_objeto_na_matriz(self,obj,jogador):
        for j in range(len(jogador.lista_de_comparacao)):
            for i in jogador.lista_de_comparacao[j]:
                if obj == i and obj not in jogador.lista_matriz:
                    index=jogador.lista_de_comparacao[j].index(obj)
                    if jogador.lista_matriz[j][index]=='X':
                        return False
                    if jogador.lista_matriz[j][index] not in self.lista_siglas:
                        return False
                    else:
                        jogador.lista_matriz[j][index]='X'
                        return True

    def checar_siglas_em_cada_posicao(self,pos,direcao,obj):
        for j in range(len(self.lista_matriz)):
            for i in range(len(self.lista_matriz[j])):
                if pos == self.lista_matriz[i][j]:
                    for k in range(obj.tamanho):
                        if direcao == 'cima':
                            if self.lista_matriz[i - k][j] in self.lista_siglas:
                                return False
                        if direcao == 'baixo':
                            if self.lista_matriz[i + k][j] in self.lista_siglas:
                                return False
                        if direcao == 'esquerda':
                            if self.lista_matriz[i][j - k] in self.lista_siglas:
                                return False
                        if direcao == 'direita':
                            if self.lista_matriz[i][j + k] in self.lista_siglas:
                                return False
                    else:
                        return True

    #obj=Navio
    #pos=posicao na matriz
    #direcao=direcao que o navio vai ser posto na matriz
    def alterar_matriz(self,pos,direcao,obj):
        if self.checar_siglas_em_cada_posicao(pos, direcao, obj):
            for j in range(len(self.lista_matriz)):
                for i in range(len(self.lista_matriz[j])):
                    if pos == self.lista_matriz[i][j]:
                        tamanho = obj.tamanho
                        for k in range(tamanho):
                            if direcao=='cima':
                                self.lista_matriz[i-k][j] = obj.sigla
                            if direcao == 'baixo':
                                self.lista_matriz[i+k][j] = obj.sigla
                            if direcao == 'esquerda':
                                self.lista_matriz[i][j-k] = obj.sigla
                            if direcao == 'direita':
                                self.lista_matriz[i][j+k] = obj.sigla
            return True
        else:
            return False

    def criar_navio(self):
        lista_navio_jogador=[]
        lista_navios = ['Porta aviões (1x5)', 'Encouraçado (1x4)', 'Cruzador (1x3)', 'Destroyer (1x2)','Destroyer (1x2)','Submarino (1x1)','Submarino (1x1)']
        lista_tamanho_navios=[5,4,3,2,2,1,1]
        lista_siglas = ['P','E','C','D','D','S','S']
        for navio in range(len(lista_navios)):
            navio_obj = Navio(lista_navios[navio], lista_tamanho_navios[navio],lista_siglas[navio])
            lista_navio_jogador.append(navio_obj)
        return lista_navio_jogador

    def posicionar_navio(self,jogador):
        posicionamento_navios=jogador.navio.copy()
        jogador.criar_matriz_asci()
        while posicionamento_navios != []:
            for i in range(len((posicionamento_navios))):
                continuar_jogo_true_ou_false=True
                while continuar_jogo_true_ou_false:
                    pos=input(f"Em qual posiçao você quer posicionar o {jogador.navio[i].nome}? (Exemplo: 6E) ").upper()
                    if jogador.percorrer_matriz(pos):
                        while continuar_jogo_true_ou_false:
                            orientacao = input("qual orientaçao do navio? 'cima','baixo','esquerda','direita'")
                            if orientacao == 'cima' or orientacao == 'baixo' or orientacao == 'esquerda' or orientacao == 'direita':
                                continuar_jogo_true_ou_false=jogador.checar_orientacao(pos,orientacao,jogador,posicionamento_navios,i)
                            else:
                                print("insira uma orientacao correta")
                    else:
                        print("essa posiçao nao está disponivel")

    def checar_orientacao(self,pos,orientacao,jogador,posicionamento_navios,i):
        if self.alterar_matriz(pos, orientacao, jogador.navio[i]):
            posicionamento_navios.remove(jogador.navio[i])
            print(self.criar_matriz_asci())
            return False
        else:
            print("Haverá um conflito com outros navios nessa posição, favor escolher outra posição")
            return True

    def chechar_campo_do_outro_jogador(self,jogada,jogador):
        if jogador.alterar_objeto_na_matriz(jogada, jogador):
            print('Você acertou o inimigo')
            jogador.criar_matriz_ascii_escondendo_navios()
        else:
            print("Você errou o inimigo")

    def continuar_jogo_ate_nao_ter_barcos(self,jogador):
        for j in range(len(jogador.lista_matriz)):
            for i in jogador.lista_matriz[j]:
                if i in ['P', 'E', 'C', 'D', 'S']:
                    return True
        else:
            return False