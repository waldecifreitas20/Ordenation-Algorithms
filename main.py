from os import system
from time import sleep
from json import loads as json

from controller.controller import checkModule, startalltests
from modules.essentials_imports import *
from views.views import *

#CARREGA DADOS DA BASE DE DADOS E RETORNA JSONS
def init():
    global ENTRIES, CASES
    ALGORITHMS = ('bubblesort', 'countingsort', 'mergesort')

    #CONVERTE OS DADOS EM JSON
    jsons = []
    for algorithm in ALGORITHMS:
        for case in CASES:
            for n in ENTRIES:
                file_name = f'{algorithm.upper()}_{case}_{n}.json'
                path = f'database/{algorithm}/{file_name}'
                with open(path, 'r', encoding='utf-8') as file:
                    to_json = file.read()
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

#APRESENTA DADOS PRE E POS ORDENAÇÃO
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
        print('SALVANDO DADOS...')
        datasaver(module, case, length)
        print('DADOS SALVOS COM SUCESSO!')

#VERIFICA A ESCOLHA DO USUARIO
def checkchoice():
    choice = int(input('ESCOLHA UMA OPCAO: '))

    if choice == 0:
        return True
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
        startalltests()
    stop = input('DESEJA VOLTAR AO MENU PRINCIPAL?(s/n)\nR: ')

    return stop == 's'

#RETORNA CASO E TAMANHO DO VETOR
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

#SALVA DADOS NA BASE DE DADOS
def datasaver(module, case, length):
    global CASES, ENTRIES
    data = filesaver.setData(module.getRuntime(), module)
    filesaver.saveAsJson(f'{CASES[case]}_{ENTRIES[length]}', module.NAME, data)



#VARIAVEIS DE CONSULTA
CASES = ('WORST', 'RANDOM')
ENTRIES = ('10','100','1000','10000','20000')
CASES_VALUES = (casestest.WORSTS_CASES, casestest.RANDOM_CASES)

#DADOS PRE-INICIALIZADOS EM JSON
ALGORITHMS_DATA = list(init())

stop = False
while(not stop):    
    mainmenu()
    stop = checkchoice()

finalize()
