''' Урок 2. Циклы. Рекурсия. Функции.
4. Найти сумму n элементов следующего ряда чисел:
1 -0.5 0.25 -0.125 ...Количество элементов (n) вводится с клавиатуры.'''
import time

start = time.time()


def summ(arq):
    if not arq:
        return 0
    else:
        res = summ(arq[1:])
        res = res + arq[0]
        return res

def sum2(arq):
    return sum(arq)

def sum3(arq):
    res = 0
    for i in arq:
        res += i
    return res



if __name__ == '__main__':
    arq = [float(i) for i in input('Введите ряд чисел: ').split()]
    print(summ(arq))
    print(sum2(arq))
    print(sum3(arq))
    print(time.time() - start)

#деньги только decimal, не float

