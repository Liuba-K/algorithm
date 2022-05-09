'''Урок 2. Циклы. Рекурсия. Функции.
3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843.'''
import math
import time

start = time.time()


def reverse(numb):
    # 1. Проверка, корректно ли число
    if numb < 0:
        return f'вы ввели отрицательное число'
    if numb == 0:
        return 0
    n = 0  # порядок числа
    num2 = numb  # копия num?
    while num2 > 0:
        n = n + 1
        num2 = num2 // 10
    t = numb % 10  # взять последнее число
    res = t * int(math.pow(10, n - 1))  # умножить последнюю цифру на 10^n
    return res + reverse(numb // 10)


print(reverse(int(input('введите число: '))))

print(time.time() - start)
