#MODULO DE FUNCOES E VARIAVEIS AUXILIARES

NUMBER_TEST = 20

def showinitmessage(algorithm_name, case, array_length):
    print('*'*50)
    print(f'# INICIANDO TESTES COM {algorithm_name}...')
    print(f'    CASO DO TIPO: {case}')
    print(f'    TAMANHO DA ENTRADA: {array_length}')

def showfinalmessage(algorithm_name):
    print(f'TESTES COM {algorithm_name} FINALIZADOS!')
    print('*'*50)

def updateruntime(runtime, number_test):
    return runtime/number_test
