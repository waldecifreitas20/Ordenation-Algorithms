from modules import (
    bubblesort as bubble,
    mergesort as merge,
    countingsort as counting,
    casestest as CASES,
    filesaver
)

def showinitmessage(algorithm_name, case, array_length):
    print('*'*50)
    print(f'# INICIANDO TESTES COM {algorithm_name}...')
    print(f'          CASO DO TIPO: {case}')
    print(f'    TAMANHO DA ENTRADA: {array_length}')

def showArray(array, moment):
    print(f'\nVETOR {moment}-ORDENACAO: {array}\n')

def showfinalmessage(algorithm_name):
    print(f'TESTES COM {algorithm_name} FINALIZADOS!')
    print('*'*50)

def updateruntime():
    global runtime, NUMBER_TEST
    runtime /= (NUMBER_TEST)

def updatecase(_case, _length):
    global case, length
    case = _case
    length = _length

runtime, length, case = int, int, str 
NUMBER_TEST = 20

#PIORES CASOS:
showArray(CASES.WORST_CASE_10, 'PRE')

# COM 10 ELEMENTOS 
updatecase('WORST_10', len(CASES.WORST_CASE_10))

# - TESTE BUBBLE SORT
showinitmessage(bubble.NAME, 'PIOR', length)
runtime = 0
for n in range(NUMBER_TEST):
    ordered_array = bubble.bubblesort(CASES.WORST_CASE_10)
    runtime += bubble.getRuntime()
updateruntime()
showArray(ordered_array, 'POS')

DATA_BUBBLE_WORST_10 = filesaver.setData(runtime, bubble)
filesaver.saveAsJson(case, bubble.NAME, DATA_BUBBLE_WORST_10)
showfinalmessage(bubble.NAME)


# - TESTE MERGE SORT
showinitmessage(merge.NAME, 'PIOR', length)
runtime = 0
for n in range(2):
    ordered_array = merge.mergesort(CASES.WORST_CASE_10)
    runtime += merge.getRuntime()
updateruntime()
showArray(ordered_array, 'POS')

DATA_MERGE_WORST_10 = filesaver.setData(runtime, merge)
filesaver.saveAsJson(case, merge.NAME, DATA_MERGE_WORST_10)


# - TESTE COUNTING SORT
showinitmessage(counting.NAME, 'PIOR', length)
runtime = 0
for n in range(2):
    ordered_array = counting.countingsort(CASES.WORST_CASE_10)
    runtime += counting.getRuntime()
updateruntime()
showArray(ordered_array, 'POS')

DATA_COUNTING_WORST_10 = filesaver.setData(runtime, counting)
filesaver.saveAsJson(case, counting.NAME, DATA_COUNTING_WORST_10)


# COM 100 ELEMENTOS




print('TODOS OS TESTES FORAM FINALIZADOS')
