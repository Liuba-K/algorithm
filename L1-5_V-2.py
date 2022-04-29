#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

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
  print(numb_letter(
    input('Введите букву русского алфавита: '),
    input('Введите вторую букву русского алфавита: ')
  ))