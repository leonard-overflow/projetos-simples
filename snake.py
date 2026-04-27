import numpy
import readchar

tabuleiro = numpy.full((10, 15), " ")

snake = ["O", "O"]

tabuleiro[4, 2] = snake[0]
tabuleiro[4, 3] = snake[1]

print("Bem-vindo ao snake game(Sair 0")

print(tabuleiro)

while True:
    print("Para qual direcao voce quer ir?")

    resposta = readchar.readkey()

    if resposta == "0":
        break
    elif resposta == readchar.key.UP or resposta == "w":
        print("Cima")
    elif resposta == readchar.key.DOWN or resposta == "s":
        print("Baixo")
    elif resposta == readchar.key.LEFT or resposta == "a":
        print("Esquerda")
    elif resposta == readchar.key.RIGHT or resposta == "d":
        print("Direita")
    else:
        continue