#5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.
# если без буквы ё
def numb_letter(start,finish):  
  numb1 = ord(start.lower()) - 1071
  numb2 = ord(finish.lower()) - 1071
  if numb1 >= numb2:
    dif = numb1 - numb2 - 1
    return f'{numb1}, {numb2}, между ними {dif} букв(а)'
  elif numb1 < numb2:
    dif = numb2 - numb1 - 1
    return f'{numb1}, {numb2}, между ними {dif} букв(а)'
  else:
    return f' Вы не верно ввели данные'
  
if __name__ == '__main__':
  print(numb_letter(
    input('Введите букву русского алфавита'),
    input('Введите вторую букву русского алфавита')
  ))