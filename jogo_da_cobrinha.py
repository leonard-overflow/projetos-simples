import numpy

tabuleiro = numpy.full((10, 15), " ")

snake = ["O", "O"]
fruta = ["*"]

tabuleiro[4, 2] = snake[0]
tabuleiro[4, 3] = snake[1]

print("Bem-vindo ao snake game(Sair 0")

print(tabuleiro)

while True:
    resposta = input("Para qual direcao voce quer ir?: ")

    match resposta:
        case "0":
            break
        case