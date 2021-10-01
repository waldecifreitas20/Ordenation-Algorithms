#EM CASO DE DUVIDAS A RESPEITO DESTE PROGRAMA, CONSULTE O AQUIVO "README.MD"

""" 
CASES:
    .WORST_CASES: PIORES CASOS
    .RANDOM_CASES: CASOS ALEATORIOS
        -> [0]: 10 ELEMENTOS
        -> [1]: 100 ELEMENTOS
        -> [2]: 1000 ELEMENTOS
        -> [3]: 10000 ELEMENTOS
        -> [4]: 100000 ELEMENTOS    
"""

from tests import tests as test
from modules import (
    bubblesort as bubble,
    mergesort as merge,
    countingsort as counting,
    casestest as CASES
)

modules = (bubble, merge, counting)

#REALIZA TODOS OS TESTES DE PIOR CASO PARA TODOS OS ALGORITMOS
for module in range(3):
    for case in range(len(CASES.WORSTS_CASES)):
        test.worst_case(CASES.WORSTS_CASES[case], modules[module])

#REALIZA TODOS OS TESTES DE CASOS ALEATORIOS PARA TODOS OS ALGORITMOS
for module in range(3):
    for case in range(len(CASES.RANDOM_CASES)):
        test.random_case(CASES.RANDOM_CASES[case], modules[module])
