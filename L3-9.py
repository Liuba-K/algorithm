#9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
import numpy as np
n, m = 4, 5
a = [[int(random() * 11) - 5 for j in range(m)] for i in range(n)]
a=np.array(a) 

d = sum(a[:,0])
m = np.amax(a[:,0])
for i in range(1, a.shape[0]):  
  if d > sum(a[:,i]):
    m = np.amax(a[:,i])       
print("Максимальный элемент среди минимальных элементов столбцов матрицы:", m)