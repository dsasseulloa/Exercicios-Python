from Cartas import Cartas
from Jogador import Jogador
from Mesa import Mesa

jogador=Jogador([])
cartas=Cartas(['2','3','4','5','6','7','8','9','10','A','J','Q','K'])
mesa = Mesa
cartas_baralho=cartas.cartas
cartas_escolhidas = jogador.cartas_viradas
cartas_embaralhadas = cartas.embaralhar_cartas(cartas_baralho)



mesa.Jogo(mesa,cartas,jogador,cartas_embaralhadas)
