import pyautogui
from time import sleep 
from pynput import mouse

def on_move(x, y):
    print('Posição atual do mouse: ({0}, {1})'.format(x, y))

# Cria uma instância do listener do mouse
listener = mouse.Listener(on_move=on_move)

# Inicia o listener
listener.start()

# Mantém o programa em execução para que as coordenadas do mouse sejam atualizadas
listener.join()
