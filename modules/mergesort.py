from time import time

_comparasions,_swaps = 0,0
_FINAL_TIME,_INITAL_TIME = None,None
NAME = 'MERGESORT'

def merge1(array):
    global _comparasions, _INITAL_TIME
    _comparasions += 1
    _INITAL_TIME = time()

    if len(array) <= 1:
        return array
    middle = len(array)//2
    left = merge1(array[0:middle])
    right = merge1(array[middle:])

    return merge2(left, right)

def merge2(array_left, array_right):
    global _comparasions,_swaps
    i,j = 0,0
    ordered_list = list()
    is_end_left,is_end_right = False, False
    length = len(array_left + array_right)
    
    for _ in range(length):
        _comparasions += 1
        if not is_end_left and not is_end_right:
            _comparasions += 1
            if array_left[i] <= array_right[j]:
                ordered_list.append(array_left[i])
                i += 1
            else:
                _swaps += 1
                ordered_list.append(array_right[j])
                j += 1
        
        elif not is_end_left:
            _comparasions += 1
            ordered_list.append(array_left[i])
            i += 1
        elif not is_end_right:
            _comparasions += 1
            ordered_list.append(array_right[j])
            j += 1
        else:
            _comparasions += 3

        if i >= len(array_left): is_end_left = True
        if j >= len(array_right): is_end_right = True
        _comparasions += 2


    return ordered_list

def mergesort(array):
    global _FINAL_TIME, _comparasions,_swaps
    _comparasions,_swaps = 0,0
    new_array = merge1(array)
    _FINAL_TIME = time() - _INITAL_TIME

    return new_array

def getComparasions():
    return _comparasions

def getSwaps():
    return _swaps

def getRuntime():
    return _FINAL_TIME
