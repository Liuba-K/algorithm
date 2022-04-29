#9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

def median(*arqs):
  if (arqs[0]>arqs[1] and arqs[0] < arqs[2]) or (arqs[0] < arqs[1] and arqs[0] > arqs[2]):
    return f'{arqs[0]} явлется средним числом'
  elif (arqs[1]>arqs[2] and arqs[1] < arqs[0]) or (arqs[1] < arqs[2] and arqs[1] > arqs[0]):
    return f'{arqs[1]} явлется средним числом'
  elif (arqs[2]>arqs[1] and arqs[1] < arqs[0]) or (arqs[2] < arqs[1] and arqs[1] > arqs[0]):
    return f'{arqs[2]} явлется средним числом'
  else:
    return f'Числа: {arqs} нет одного среднего числа'

if __name__ == '__main__':
  print(median(
    int(input('Введите число 1: ')),
    int(input('Введите число 2: ')),
    int(input('Введите число 3: '))
))