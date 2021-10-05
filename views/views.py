#MODULO DE APRESENTACAO DE TELAS

from os import system, name
from time import sleep

#SIMULA UM ENCERRAMENTO
def mainmenu():
    print("""\n
=========================================
            MENU PRINCIPAL
=========================================
1) BUBBLE SORT
2) COUNTING SORT
3) MERGE SORT
4) VISUALIZAR DADOS SALVOS
5) ATUALIZAR BASE DE DADOS (TESTE GERAL)
0) FECHAR PROGRAMA
=========================================""")

def finalize():
    for _ in range(2):
        if name == 'nt':
           _windowsloading(0.4)
        else:
          _linuxloading(0.4)
    _showabout()    

def _windowsloading(time):
    system('cls')
    print('[|] -> ENCERRANDO APLICACAO.')
    sleep(time)

    system('cls')
    print('[/] -> ENCERRANDO APLICACAO..')
    sleep(time)
    
    system('cls')
    print('[-] -> ENCERRANDO APLICACAO..')
    sleep(time)

    system('cls')
    print('[\\] -> ENCERRANDO APLICACAO...')
    sleep(time)

def _linuxloading(time):
    system('clear')
    print('[|] -> ENCERRANDO APLICACAO.')
    sleep(time)

    system('clear')
    print('[/] -> ENCERRANDO APLICACAO..')
    sleep(time)
    
    system('clear')
    print('[-] -> ENCERRANDO APLICACAO..')
    sleep(time)

    system('clear')
    print('[\\] -> ENCERRANDO APLICACAO...')
    sleep(time)


def _showabout():
    system('clear')
    print("""
    DESENVOLVIDO POR: WALDECI FREITAS, WALFREDO FILHO & ALAN BITTENCOURT
    VERSÃO: 3.9 - 01/10/21
    GitHub: https://github.com/waldecifreitas20/Ordenation-Algorithms/

    OBRIGADO POR UTILIZAR NOSSO PROGRAMA!
    """)