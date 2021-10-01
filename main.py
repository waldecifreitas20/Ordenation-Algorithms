from os import popen
from os.path import abspath

def getPaths():
    ALGORITHMS = ('bubblesort', 'countingsort', 'mergesort')
    CASES = ('RANDOM', 'WORST')
    ENTRIES = (10,100,1000,10000,20000)

    PATHS = []

    for algorithm in ALGORITHMS:
        for case in CASES:
            for n in ENTRIES:
                file = f'{algorithm.upper()}_{case}_{n}.json'
                relative = f'results/{algorithm}/{file}'
                PATHS.append(abspath(relative))

    return PATHS

PATHS = getPaths()
for path in PATHS:
    with open(path, 'r', encoding='utf-8') as path:
        print(path.readable())