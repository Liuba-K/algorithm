#1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
#Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде комментариев к коду. Также укажите в комментариях версию Python и разрядность вашей ОС.

import sys
'''
L_5-2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections
'''

#Выделено памяти 56 байт
#Временная сложность: O(1)
# так как у нас только два элемента
#Пространственная сложность: O(1)


def sum_multiplication(number_1, number_2):
  number_1 = ''.join(number_1)
  number_2 = ''.join(number_2)
  Sum = hex(int(number_1, 16)+ int(number_2, 16))
  Sum = Sum.split('0x')[1].upper()
  multiplication = hex(int(number_1, 16) * int(number_2, 16))
  multiplication = list(''.join(multiplication.split('0x')[1]).upper())
  return(list(''.join(Sum)), multiplication)

if __name__ == '__main__':
  number_1 = input('Введите шестнадцатеричное число через пробел: ').split()
  number_2 = input('Введите второе шестнадцатеричное число через пробел: ').split()  
  print(sum_multiplication(number_1, number_2))
  print(sys.getsizeof(sum_multiplication(number_1, number_2)))

''' 
L1-4. Написать программу, которая генерирует в указанных пользователем границах:
-случайное целое число;
-случайное вещественное число;
-случайный символ.
-Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
'''
import random
import string

def random_number(start,finish):
  if start.isdigit() and finish.isdigit():
    print(random.randrange(int(start),int(finish)))
  elif start.replace('.','',1).isdigit() and finish.replace('.','',1).isdigit():
    print(random.uniform(float(start),float(finish)))
  elif start in string.ascii_letters and finish in string.ascii_letters:
    letters_choice = string.ascii_letters[string.ascii_letters.find(start) + string.ascii_letters.find(finish)]
    print(random.choice(letters_choice)) #работает правильно?
  else:
    return f'вы ввели некорректные данные'#почему-то не выкидывает этот результат

if __name__ == '__main__':
  start = input('введите границу диапазона (букву английского алфавита): ')
  finish = input('введите вторую границу диапазона(букву английского алфавита): ') 
  random_number(start,finish)
  print(sys.getsizeof(random_number(start,finish)))

#Выделено памяти 16 байт
#Временная сложность: O(N) -так как только if
#Пространственная сложность: O(1) - только входные данные


'''
1.5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
'''
#print(*(chr(i) for i in range(1072, 1105)), sep='')
alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def numb_letter(start,finish):
  if len(start) > 1 or len(finish) > 1:
    return f'Вы ввели в строчку больше одного символа'
  if len(start) == 0 or len(finish) == 0:
    return f'Вы не ввели в каждую строчку по букве'
  if start.lower() in alphabet and finish.lower() in alphabet:
    numb1 = alphabet.find(start.lower()) + 1
    numb2 = alphabet.find(finish.lower()) + 1
    if numb1 > numb2:
      dif = numb1 - numb2 -1
      return f'{numb1}, {numb2}, между ними {dif} букв(а/ы)'
    elif numb1 < numb2:
      dif = numb2 - numb1 - 1
      return f'{numb1}, {numb2}, между ними {dif} букв(а/ы)'
    else:      
      return f'{numb1}, {numb2}, между ними нет букв'
  else:
    return f'Вы ввели не русские буквы'
    
if __name__ == '__main__':
  start = input('Введите букву русского алфавита: ')
  finish = input('Введите вторую букву русского алфавита: ')
  print(numb_letter(start,finish))
  print(sys.getsizeof(numb_letter(start,finish)))

#Выделено памяти 134 байт (варьирует от букв: 124-134)
#Временная сложность: O(N**2) -так как два if, второй вложенный
#Пространственная сложность: O(N**2) - поиск в последовательности дважды
