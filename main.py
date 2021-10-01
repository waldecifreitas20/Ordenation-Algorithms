from os import system
from os.path import abspath
from json import loads as json
from time import sleep
def init():
    global ENTRIES
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

        
#VARIAVEIS DE CONSULTA
CASES = ('RANDOM', 'WORST')
ENTRIES = ('10','100','1000','10000','20000')

#DADOS DOS ALGORITMOS EM JSON
ALGORITHMS_DATA = list(init())

stop = 's'
while(stop.lower() != 'n'):    

    print("""\n
    =========================================
                MENU PRINCIPAL
    =========================================
    1) DADOS BUBBLE SORT
    2) DADOS COUNTING SORT
    3) DADOS MERGE SORT
    4) VISUALIZAR TODOS OS DADOS SALVOS
    0) FECHAR PROGRAMA
    =========================================""")
    choice = int(input('ESCOLHA UMA OPCAO: '))

    if choice == 0:
        break
    if choice == 4:
        for algorithm in ALGORITHMS_DATA:
            showdata(algorithm)
    else:
        showdata(ALGORITHMS_DATA[choice-1])

    stop = input('DESEJA VOLTAR AO MENU PRINCIPAL?(s/n)\nR: ')

finalize()
print("""
DESENVOLVIDO POR: WALDECI FREITAS, WALFREDO FILHO & ALAN BITTENCOURT
VERSÃO: 3.3 - 01/10/21
GitHub: https://github.com/waldecifreitas20/Ordenation-Algorithms/

OBRIGADO POR UTILIZAR NOSSO PROGRAMA!
""")
