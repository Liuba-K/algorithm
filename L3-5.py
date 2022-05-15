#5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
from random import random

def max_negative_element(spisok):
  if str(min(spisok))[0] == '-':
    return(f'значение максимального отрицательного элемента {min(spisok)}, а позиция: {spisok.index(min(spisok))}')
  else:
    return(f'в этом массиве нет отрицательных элементов')

if __name__ == '__main__':
  spisok = [int(random() * 11) - 5 for i in range(20)] 
  print(max_negative_element(spisok))