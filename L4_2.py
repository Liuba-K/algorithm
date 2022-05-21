import time
import cProfile
#import random

start = time.time()
#Без использования «Решета Эратосфена»;
def without_Eratosthenes_sieve(sieve, found):
  #flag = True
  for num in sieve:
    prost_set = []
    for i in range(2, num):
        #print(i)
        for j in range(2, i):
        #for j in prost_set:
            #print(f'{num} {i} {j} {i % j}')
            if i % j == 0: #нужно другое условие
                break
        else:

            prost_set.append(i)
            for ind, n in enumerate(prost_set):
                if ind == found:
                    return n
                    break


print(time.time() - start)
print('-' * 20)

start1 = time.time()
def with_Eratosthenes_sieve(sieve, found):
    prost_set2 = set()
    while sieve:
        prime = min(sieve)  # min простое
        #print(prime)
        prost_set2.add(prime)
        for i, res in enumerate(sorted(prost_set2)):
            if i == found:
                return res
                break
        sieve -= set(range(prime, n + 1, prime))


print(time.time() - start1)
print('-' * 20)

def main():
    print(without_Eratosthenes_sieve(sieve, found))
    print(with_Eratosthenes_sieve(sieve, found))

if __name__ == '__main__':
    #sieve = [random.randrange(-5, 5) for _ in range(10**6)]
    n = int(input('до какого числа '))
    sieve = set(range(2, n + 1))
    found = int(input('какой элемент найти среди простых чисел  '))
    #print(without_Eratosthenes_sieve(sieve, found))
    #print(with_Eratosthenes_sieve(sieve, found))
    cProfile.run('main()')
     #cProfile.run(f'without_Eratosthenes_sieve({sieve}, {found})')
     #cProfile.run(f'with_Eratosthenes_sieve({sieve}, {found})')
