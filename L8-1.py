#Урок 8. Деревья. Хэш-функция
#1. Определение количества различных подстрок с использованием хэш-функции. Пусть дана строка S длиной N, состоящая только из маленьких латинских букв. Требуется найти количество различных подстрок в этой строке.

## Провести поиск подстроки в строке
#алгоритм Рабина-Карпа
import hashlib
def rabin_karp(s,t):
  len_sub = len(t)  
  h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()  
  #print(h_subs)
  if len(s)<1:
    return f'строка не введена'
  elif len(s)< len_sub:
    return f'Подстрока больше строки'
  elif len(s)== len_sub:
    return 1
  else:
    n=0
    for i in range(len(s) - len_sub + 1):      
      #print(f'i={i}, n={n}, {s[i:i+len_sub]}')
      #print(f'i= {i}, {len(s)}, {s[i:i+len_sub]},  {s[i+len_sub]}')
      if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
        n+=1        
      
    return n+1


if __name__ == '__main__': 
  print(rabin_karp(
    input("Введите строку: "),
    input("Введите интересующую подстроку: ")))

"""
  N = int(input("введите длину строки: "))
  spisok = []
  for i in range(N):
    spisok.append([])
    print(i)    
    spisok[i].append(input(f"введите букву{i+1}: "))  
  print(rabin_karp(N,str(spisok),input("Введите интересующую подстроку: ")))
"""