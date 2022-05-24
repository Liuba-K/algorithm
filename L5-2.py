#Урок 5. Коллекции. Список. Очередь. Словарь.
#2. Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив, элементы которого это цифры числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
#Примечание: для решения задач попробуйте применить какую-нибудь коллекцию из модуля collections

#hex(х) - преобразование целого числа в шестнадцатеричную строку.

def sum_multiplication(number_1, number_2):
  number_1 = ''.join(number_1)
  number_2 = ''.join(number_2)
  Sum = hex(int(number_1, 16)+ int(number_2, 16))
  Sum = Sum.split('0x')[1]
  multiplication = hex(int(number_1, 16) * int(number_1, 16))
  multiplication = list(''.join(multiplication.split('0x')[1]))
  return(list(''.join(Sum)), multiplication)

if __name__ == '__main__':
  number_1 = input('Введите шестнадцатеричное число через пробел: ').split()
  number_2 = input('Введите второе шестнадцатеричное число через пробел: ').split()
  print(type(number_1), number_2, number_1)
  print(sum_multiplication(number_1, number_2))