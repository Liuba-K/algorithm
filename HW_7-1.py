#1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив, заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы. Сортировка должна быть реализована в виде функции. По возможности доработайте алгоритм (сделайте его умнее).

import random

#O(n**2)
def bubble_sort(spisok):
    swapped = False
    for i in range(len(spisok) - 1, 0, -1):
        #print(f'i={i}')
        for j in range(i):            
            if spisok[j] < spisok[j + 1]:
                #print(spisok[j],spisok[j + 1])
                spisok[j + 1], spisok[j] = spisok[j], spisok[j + 1]
                swapped = True
                #print(spisok)
        if swapped:
            swapped = False
        else:
            break
 
    return spisok

if __name__ == '__main__':
    s = [random.randrange(-100, 100) for i in range(10**2)]
    print(f'Исходный массив {s}')
    print(*bubble_sort(s))
