from os import system
from os.path import abspath
from json import loads as json
from time import sleep
from __init__ import startTests
from modules import (
    bubblesort as bubble,
    mergesort as merge, 
    countingsort as counting,
    casestest
)

def init():
    global ENTRIES, CASES
    ALGORITHMS = ('bubblesort', 'countingsort', 'mergesort')
    

    #CARREGA OS DIRETORIOS DE TODOS OS ARQUIVOS
    PATHS = []
    for algorithm in ALGORITHMS:
        for case in CASES:
            for n in ENTRIES:
                file = f'{algorithm.upper()}_{case}_{n}.json'
                relative = f'results/{algorithm}/{file}'
                PATHS.append(abspath(relative))

    #CONVERTE TODOS OS ARQUIVOS EM JSONS
    jsons = []
    for path in PATHS:
        with open(path, 'r', encoding='utf-8') as path:
            to_json = path.read()
            jsons.append(json(to_json))
    
    return jsons[:10], jsons[10:20], jsons[20:]

#RETORNA OS DADOS DO JSON CONVERTIDOS
def getdata(algorithm):
    global ENTRIES, CASES

    runtime, comparasions, swaps, case = (
        algorithm['runtime'],
        algorithm['comparasions'],
        algorithm['swaps'],
        algorithm['case_type']
    )
    array_length = int
    for entry in ENTRIES:
        if entry in case:
            array_length = int(entry)

    current_case = 'CASO ALEATORIO'
    if 'worst' in case:
        current_case = 'PIOR CASO'

    return (
        swaps, 
        runtime, 
        array_length,
        current_case, 
        comparasions 
    )

#MOSTRA OS DADOS DO ALGORITMO
def showdata(algorithm_data):
    name = algorithm_data[0]['algorithm']
    print('\n\n=========================================')
    print(f'        DADOS {name}')
    print('=========================================')
    for algorithm in algorithm_data:
        (
            swaps, 
            runtime, 
            array_length, 
            current_case, 
            comparasions
        ) = getdata(algorithm)

        print(f'[+] PARA {current_case} - {array_length} ELEMENTOS:\n')    
        print(f'TROCAS EFETUADAS: {swaps}')
        print(f'No. COMPARACOES: {comparasions}')
        print('TEMPO DE EXECUCAO(s): {:.3f}'.format(float(runtime)))    
        print('-----------------------------------------')

def cleanscreen():
    system('cls')

def finalize():
    for _ in range(2):
        print('FECHANDO APLICACAO.')
        sleep(0.3)
        cleanscreen()
        print('FECHANDO APLICACAO..')
        sleep(0.3)
        cleanscreen()
        print('FECHANDO APLICACAO...')
        sleep(0.3)
        cleanscreen()
    print("""
    DESENVOLVIDO POR: WALDECI FREITAS, WALFREDO FILHO & ALAN BITTENCOURT
    VERSÃO: 3.5 - 01/10/21
    GitHub: https://github.com/waldecifreitas20/Ordenation-Algorithms/

    OBRIGADO POR UTILIZAR NOSSO PROGRAMA!
    """)


def getcasetest(algorithm_name):
    print(f"""\n
    =========================================
                MENU {algorithm_name}
    =========================================
    [-] ESCOLHA O TAMANHO DO VETOR A SER ORDENADO: 
        0) 10
        1) 100
        2) 1000
        3) 10000
        4) 20000
    -----------------------------------------""")
    length = int(input('    R: '))
    print("""
    -----------------------------------------
    [-] ESCOLHA O CASO: 
        0) ORDEM DECRESCENTE
        1) VALORES ALEATORIOS
    -----------------------------------------""")
    case = int(input('    R: '))

    return case,length

def checkModule(module, array):
    if module.NAME == 'BUBBLESORT':
        return module.bubblesort(array)
    elif module.NAME == 'MERGESORT':
        return module.mergesort(array)
    else: 
        return module.countingsort(array)

def toOrder(module):
   
    case, length = getcasetest(module.NAME)
    array = CASES_VALUES[case][length]
    print(f'VETOR PRE-ORDENACAO -> {array}')
    ordered = checkModule(module,array)
    print('\n-----------------------------------------\n')
    print(f'VETOR POS-ORDENACAO -> {ordered}')
    print(f'No. COMPARACOES: {module.getComparasions()}')
    print(f'TROCAS EFETUADAS: {module.getSwaps()}')
    print(f'TEMPO DE EXECUCAO: {module.getRuntime()}\n\n')
    save = input('DESEJA SALVAR ESTES DADOS NA BASE DE DADOS?(s/n)\nR: ')
    if save.lower() == 's':
        savedate
    
def


#VARIAVEIS DE CONSULTA
CASES = ('RANDOM', 'WORST')
ENTRIES = ('10','100','1000','10000','20000')
CASES_VALUES = (casestest.WORSTS_CASES, casestest.RANDOM_CASES)

#DADOS PRE-INICIALIZADOS EM JSON
ALGORITHMS_DATA = list(init())

stop = 's'
while(stop.lower() != 'n'):    

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
    choice = int(input('ESCOLHA UMA OPCAO: '))

    if choice == 0:
        break
    elif choice == 1:
        toOrder(bubble)
    elif choice == 2:
        toOrder(counting)
    elif choice == 3:
        toOrder(merge)
    elif choice == 4:
        for algorithm in ALGORITHMS_DATA:
            showdata(algorithm)
        print('\n\n')
    elif choice == 5:
        startTests()
    stop = input('DESEJA VOLTAR AO MENU PRINCIPAL?(s/n)\nR: ')

finalize()
