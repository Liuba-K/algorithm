#7. В одномерном массиве целых чисел определить два наименьших элемента. Они могут быть как равны между собой (оба являться минимальными), так и различаться.
from random import random

def two_min(spisok):  
  ind_min = spisok.index(min(spisok))
  spisok_new = spisok[0:ind_min]+ spisok[ind_min+1:len(spisok)]
  return f' два наименьших элемента: {min(spisok)}, {min(spisok_new)}'
 
    
if __name__ == '__main__':
  N = 20
  spisok = [0] * N
  spisok = [int(random()*15) for i in range(N)] 
  print(two_min(
    spisok)
  )