#1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
start_spisok = 2 
finish_spisok = 99
spisok = [i for i in range(start_spisok,finish_spisok+1)]
#print(spisok)
list = [i for i in range(2,10)] # от 2 до 9.можно сделать как предыдущий
#print(list)
for b in list:
  multiple = []
  for i in spisok:
    if i % b == 0:
      multiple.append(i)  
  print(f'кратно {b}: {len(multiple)} чисел/ла в диапазоне от {start_spisok} до {finish_spisok}')
      