from collections import namedtuple

#SALVA OS ARQUIVOS EM FORMATO JSON
def saveAsJson(case, algorithm: str, data):
    PATH = f'./database/{algorithm.lower()}/{algorithm}_{case}.json'
    with open(PATH, mode='w', encoding='UTF-8') as database:
        database.write('{\n')
        database.write(f'   "algorithm" : "{algorithm}",\n')
        database.write(f'   "case_type" : "{case.lower()}_case",\n')
        database.write(f'   "runtime" : "{data.runtime}",\n')
        database.write(f'   "comparasions" : "{data.comparasions}",\n')
        database.write(f'   "swaps" : "{data.swaps}"\n')
        database.write('} \n')

#PREPARA OS DADOS PARA SEREM SALVOS
def setData(runtime, module):
    TUPLE_BUILER = namedtuple('data', ['runtime', 'comparasions', 'swaps'])
    
    return TUPLE_BUILER(
        runtime='{:.15f}'.format(runtime), 
        comparasions=module.getComparasions(),
        swaps=module.getSwaps()
    )