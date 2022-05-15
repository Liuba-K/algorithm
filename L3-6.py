#6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный и максимальный элементы в сумму не включать.

from random import random

# как создать и отрицательные элементы?

def sum_between_max_min(spisok):
  ind_max = spisok.index(max(spisok))
  ind_min = spisok.index(min(spisok))

  if ind_max < ind_min: 
    res = sum(spisok [ind_max+1:ind_min])
    return (f'сумма элементов: {res}')
  elif ind_min < ind_max:  
    res = sum(spisok [ind_min+1:ind_max])
    return (f'сумма элементов: {res}')
  else:
    return (f'нет элементов между минимальным и максимальным элементами')
    
if __name__ == '__main__':
  N = 20
  spisok = [0] * N
  spisok = [int(random()*15) for i in range(N)] 
  print(sum_between_max_min(
    spisok)
  )