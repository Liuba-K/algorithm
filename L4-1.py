#1. Проанализировать скорость и сложность одного любого алгоритма, разработанных в рамках домашнего задания первых трех уроков.

# Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.
import random
import time
import cProfile
#import timeit

start = time.time()

def summ(arq):
    if not arq:
        return 0
    else:
        res = summ(arq[1:])
        res = res + arq[0]
        return res
print(time.time() - start)

start1 = time.time()
def sum2(arq):
    return sum(arq)
print(time.time() - start1)

start2 = time.time()
def sum3(arq):
    res = 0
    for i in arq:
        res += i
    return res

print(time.time() - start2)

if __name__ == '__main__':
    # arq = [float(i) for i in input('Введите ряд чисел: ').split()]
    arq = [random.randrange(-5, 5) for _ in range(10**6)]
    # print(summ(arq))    
    print(sum2(arq))
    print(sum3(arq))

    # cProfile.run(f'summ({arq})') # почему выдает только один
    cProfile.run(f'sum2({arq})')
    cProfile.run(f'sum3({arq})')


