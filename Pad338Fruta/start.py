# O jogo deverá sortear uma fruta conforme a lista abaixo:
# - banana
# - jabuticaba
# - pitanga
# - mirtilo
# - morango
# - abacaxi
# - cereja
# O objetivo é acertar o nome da fruta. O jogador informa uma letra e o jogo verifica se a fruta tem essa letra.

import random

lista_frutas=['banana','jabuticaba','pitanga','mirtilo','morango','abacaxi','cereja']
fruta_escolhida=random.choice(lista_frutas)


lista_fruta_escolhida=[]
string_fruta=''
for i in fruta_escolhida:
    lista_fruta_escolhida.append(i)

lista_letra_fruta = []
for i in lista_fruta_escolhida:
        lista_letra_fruta.append('_')
jogo_continua=True

while jogo_continua:
    letra=input("Insira uma letra para verificar se existe na fruta: ")
    try:
        x = int(letra)
        print('Favor insirir letras')
    except ValueError:
        if len(list(letra)) > 1:
            print('favor digitar apenas uma letra')
            continue
        if letra in lista_fruta_escolhida:
            print('Essa letra pertence a fruta')
            for i in range(len(lista_fruta_escolhida)):
                if letra in lista_fruta_escolhida[i]:
                    lista_letra_fruta[i]=letra
            print(" ".join(lista_letra_fruta))
            print('')
        else:
            print(f'A letra "{letra}" não pertence a fruta')

        if "_" not in lista_letra_fruta:
            print("Parabéns, você ganhou o jogo")
            jogo_continua=False
