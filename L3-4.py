#4. Определить, какое число в массиве встречается чаще всего.
from random import random
import collections

N = 20
spisok = [0] * N
spisok = [int(random()*15)-5 for i in range(N)]
freq = collections.Counter(spisok).most_common(1)

print(f'число: {freq[0][0]}, в массиве {spisok}, встречается чаще всего')