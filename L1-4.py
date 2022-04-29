#4. Написать программу, которая генерирует в указанных пользователем границах:
#случайное целое число;
#случайное вещественное число;
#случайный символ.
#Для каждого из трех случаев пользователь задает свои границы диапазона. Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы. Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.
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
  random_number(
    input('введите границу диапазона: '),
    input('введите вторую границу диапазона: ')
  )