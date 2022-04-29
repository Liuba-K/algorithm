#8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.
def year(arqs):
  if arqs % 4 == 0 and arqs % 100 != 0 or arqs % 400 == 0:
    return f'{arqs} явлется високосным годом'
  else:
    return f'{arqs} явлется невисокосным годом'

if __name__ == '__main__':
  print(year(
    int(input('Введите год: '))
))