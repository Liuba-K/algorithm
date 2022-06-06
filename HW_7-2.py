#2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

import random
# merge_sort (похожи) quick sort
#нет- O(n**2)

#O(n*log(n))
def merge_sort(spisok):
    if len(spisok) > 1:
        mid = len(spisok) // 2
        leftList = spisok[:mid]
        rightList = spisok[mid:]
               
        merge_sort(leftList)
        merge_sort(rightList)
        m = 0
        n = 0        
        z = 0
        while m < len(leftList) and n < len(rightList):
            if leftList[m] <= rightList[n]:
              
              spisok[z] = leftList[m]              
              m += 1
            else:
                spisok[z] = rightList[n]
                n += 1
            z += 1
        while m < len(leftList):
            spisok[z] = leftList[m]
            m += 1
            z += 1
        while n < len(rightList):
            spisok[z]=rightList[n]
            n += 1
            z += 1
    return spisok
          
if __name__ == '__main__':
    s = [round(random.uniform(0, 50), 2) for i in range(10)]    
    print(f'Исходный массив {s}')
    print(*merge_sort(s))