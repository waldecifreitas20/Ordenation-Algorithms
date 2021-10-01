from random import randint

WORSTS_CASES = (
    list(range(10,0,-1)),
    list(range(100,0,-1)),
    list(range(1000,0,-1)),
    list(range(10000,0,-1)),
    list(range(20000,0,-1))
)

RANDOM_CASES = (
    [randint(0,10) for _ in range(10)],
    [randint(0,100) for _ in range(100)],
    [randint(0,1000) for _ in range(1000)],
    [randint(0,10000) for _ in range(10000)],
    [randint(0,20000) for _ in range(20000)]
)