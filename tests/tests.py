from modules.util import *
from modules import filesaver

#CHECA O MODULO A SER UTILIZADO
def _checkModule(module, array):
    if module.NAME == 'BUBBLESORT':
        return module.bubblesort(array)
    elif module.NAME == 'MERGESORT':
        return module.mergesort(array)
    else: 
        return module.countingsort(array)

def _test(array, case, module):
    runtime,LENGTH = 0,len(array)
    CASE = f'{case}_{LENGTH}'
    showinitmessage(module.NAME, 'PIOR', LENGTH)

    for _ in range(NUMBER_TEST):
        ordered_array = _checkModule(module, array)
        runtime += module.getRuntime()
    runtime = updateruntime(runtime, NUMBER_TEST)

    RESULTS_WORST_10 = filesaver.setData(runtime, module)
    filesaver.saveAsJson(CASE, module.NAME, RESULTS_WORST_10)

    showfinalmessage(module.NAME)

def worst_case(array, module):
    _test(array, 'WORST', module)
    
def random_case(array, module):
    _test(array, 'RANDOM', module)



