from time import time

_swaps, _comparasions = 0,0
_INITIAL_TIME, _FINAL_TIME = None, None
NAME = 'BUBBLESORT'

def bubblesort(array: list):
    global _comparasions, _swaps
    global _FINAL_TIME , _INITIAL_TIME
    new_array = array.copy()
    _comparasions, _swaps = 0,0
    _INITIAL_TIME = time()

    n = len(array)  
    for _ in range(n-1):
        for j in range(n-1):
            _comparasions += 1
            if new_array[j] > new_array[j+1]:
                aux = new_array[j]
                new_array[j] = new_array[j+1]
                new_array[j+1] = aux
                _swaps += 1

    _FINAL_TIME = time() - _INITIAL_TIME

    return new_array

def getSwaps():
    return _swaps

def getComparasions():
    return _comparasions

def getRuntime():
    return _FINAL_TIME