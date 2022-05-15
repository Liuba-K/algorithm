#3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

#import numpy as np
#b= np.random.randint(0, 100, 20) #class 'numpy.ndarray'
from random import random

N = 20
spisok = [0] * N
spisok = [int(random()*15) for i in range(N)]

print(spisok)

def change_max_min(spisok):  
  ind_max = spisok.index(max(spisok))
  ind_min = spisok.index(min(spisok))
  spisok[ind_max] = min(spisok)
  spisok[ind_min] = max(spisok)
  return spisok

print(change_max_min(spisok))