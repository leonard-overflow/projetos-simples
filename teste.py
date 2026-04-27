import msvcrt

print("Para qual direção você quer ir?: ", end="", flush=True)

tecla = msvcrt.getch()

if tecla == b'\xe0':  # seta especial
    tecla = msvcrt.getch()
    if tecla == b'H': direcao = "cima"
    elif tecla == b'P': direcao = "baixo"
    elif tecla == b'K': direcao = "esquerda"
    elif tecla == b'M': direcao = "direita"
elif tecla in (b'w', b'W'): direcao = "cima"
elif tecla in (b's', b'S'): direcao = "baixo"
elif tecla in (b'a', b'A'): direcao = "esquerda"
elif tecla in (b'd', b'D'): direcao = "direita"
else: direcao = "desconhecida"

print(direcao)