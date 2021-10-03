from time import time

_comparasions,_swaps = 0,0
_INITIAL_TIME,_FINAL_TIME = None,None
NAME = 'COUNTINGSORT'


def countingsort(array: list):
    global _swaps,_INITIAL_TIME,_FINAL_TIME

    _swaps = 0
    _INITIAL_TIME = time()

    bigger =  max(array)
    counter_array = [0 for _ in range(bigger+1)]

    for i in range(len(array)):
        counter_array[array[i]] += 1
   
    for i in range(len(counter_array)-1):
        counter_array[i+1] = counter_array[i] + counter_array[i+1]
    
    ordered_array = list(range(len(array)))

    for i in range(len(array)):
        counter_array[array[i]] -= 1
        index = counter_array[array[i]]
        ordered_array[index] = array[i]
        _swaps += 1
    
    _FINAL_TIME = time() - _INITIAL_TIME

    return ordered_array

def getSwaps():
    return _swaps

def getComparasions():
    return _comparasions

def getRuntime():
    return _FINAL_TIME
