import numpy as np
import readchar as rc
from classes import snake

def movimentar(direcao:str, tabuleiro:np.ndarray, cobra:snake):
    cabeca = cobra.corpo["cabeca"]

    cobra.corpo["cabeca"][0] -= 1

    if direcao == rc.key.UP or resposta == "w":

        novo_corpo = []

        for item in reversed(cobra.corpo["corpo"]):
            item = next(item, cabeca)
            novo_corpo.append(item)

    if cobra.corpo["cabeca"] in cobra.corpo["corpo"]:
        print("Game Over")

    elif resposta == rc.key.DOWN or resposta == "s":
        pass
    elif resposta == rc.key.LEFT or resposta == "a":
        pass
    elif resposta == rc.key.RIGHT or resposta == "d":
        pass

tabuleiro = np.full((10, 15), " ")

corpo = {
    "cabeca" : [4, 3],
    "corpo" : [[4, 2], [4, 1]]
}

cobra = snake(corpo, 2)

tabuleiro[tuple(snake["cabeca"])] = "0"
tabuleiro[tuple(snake["corpo"])] = "0"

print("Bem-vindo ao snake game(Sair 0")

while True:
    print(tabuleiro)

    print("Para qual direcao voce quer ir?")

    resposta = rc.readkey()

    if resposta == "0":
        break
    elif resposta == rc.key.UP or resposta == "w" or resposta == rc.key.DOWN or resposta == "s" or resposta == rc.key.LEFT or resposta == "a" or resposta == rc.key.RIGHT or resposta == "d":
        movimentar(resposta, tabuleiro, cobra)
    else:
        continue