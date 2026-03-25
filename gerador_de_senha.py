from random import randint
import string

lista_de_letras_e_numeros = string.ascii_lowercase + string.ascii_uppercase + string.digits
lista_de_simbolos = ("!@#$%&*()-_=+")
lista = lista_de_letras_e_numeros + lista_de_simbolos

while True:
    tamanho = int(input("Tamanho da senha: "))

    lista_senha = []

    if isinstance(tamanho, int) and tamanho > 0:
        for i in range(0, tamanho):
            index_char = randint(0, len(lista) - 1)
            lista_senha.append(lista[index_char])
        break
    else:
        print("Insira um número inteiro!!!")

senha = "".join(lista_senha)

print(senha)