#Пользователь вводит номер буквы в алфавите. Определить, какая это буква.
alphabet='абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

def letter(arqs):
  if  0 < arqs <= 33:
    return alphabet[arqs-1]
  else:
    return f'Ввели не верное значение'

if __name__ == '__main__':
  print(letter(
    int(input('Введите номер русского алфавита: '))
))