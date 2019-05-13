# Programa dos dados
# ebdiel serafim <ebdielserafim12@gmail.com>

from random import randint

print("jogo de dados")

dados1 = randint(1, 6)
dados2 = randint(1, 6)
jogador1 = dados1 + dados2

dados3 = randint(1, 6)
dados4 = randint(1, 6)
jogador2 = dados3 + dados4

print("Dados 1:", dados1)
print("Dados 2:", dados2)
print("Dados 3:", dados3)
print("Dados 4:", dados4)

print("Jogador 1:", jogador1)
print("Jogador 2:", jogador2)

if jogador1 > jogador2:
    print("Jogador 1 venceu!")
else:
    if jogador2 > jogador1:
        print("Jogador 2 venceu!")
else:
    print("Empate")            