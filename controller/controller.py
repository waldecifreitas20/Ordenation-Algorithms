from modules.util import *
from modules.essentials_imports import *

#CHECA O MODULO A SER UTILIZADO
def checkModule(module, array):
    if module.NAME == 'BUBBLESORT':
        return module.bubblesort(array)
    elif module.NAME == 'MERGESORT':
        return module.mergesort(array)
    else: 
        return module.countingsort(array)

#REALIZA OS TESTES ESPECIFICADOS
def _test(array, case, module):
    runtime,LENGTH = 0,len(array)
    CASE = f'{case}_{LENGTH}'
    showinitmessage(module.NAME, 'PIOR', LENGTH)

    for _ in range(NUMBER_TEST):
        ordered_array = checkModule(module, array)
        runtime += module.getRuntime()
    runtime = updateruntime(runtime, NUMBER_TEST)

    RESULTS_WORST_10 = filesaver.setData(runtime, module)
    filesaver.saveAsJson(CASE, module.NAME, RESULTS_WORST_10)

    showfinalmessage(module.NAME)

#REALIZA TODOS TESTES POSSIVEIS
def startalltests():
    modules = (bubble, merge, counting)

    #REALIZA TODOS OS TESTES DE PIOR CASO PARA TODOS OS ALGORITMOS
    for module in range(3):
        for case in range(len(CASES.WORSTS_CASES)):
            worst_case(CASES.WORSTS_CASES[case], modules[module])
    #REALIZA TODOS OS TESTES DE CASOS ALEATORIOS PARA TODOS OS ALGORITMOS
    for module in range(3):
        for case in range(len(CASES.RANDOM_CASES)):
            random_case(CASES.RANDOM_CASES[case], modules[module])


def worst_case(array, module):
    _test(array, 'WORST', module)
    
def random_case(array, module):
    _test(array, 'RANDOM', module)
