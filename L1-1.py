#1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
numb = input("введите трехзначное число")
if len(numb) == 3:
  res_sum = int(numb[0]) + int(numb[1]) + int(numb[2])
  res_mult = int(numb[0]) * int(numb[1]) * int(numb[2])
  print(f'сумма цифер =  {res_sum}')
  print(f'произведение цифер = {res_mult}')
else:
    print("вы ввели не трехзначное число")
