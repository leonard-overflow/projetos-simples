import readchar

while True:
    tecla = readchar.readkey()
    print(repr(tecla))  # mostra os bytes reais, ex: '\xe0H'
    if tecla == 'q':
        break