#Урок 5. Коллекции. Список. Очередь. Словарь.
#1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.

#import collections

number = int(input('количество предприятий: '))

Business = {}
res = {}
s = 0

for i in range(number):
  name = input(str(i+1) +' их наименование: ')
  income = [0, 0, 0, 0]
  income[0] = int(input('прибыль за 1 квартал предприятия: '))
  income[1] = int(input('прибыль за 2 квартал предприятия: '))
  income[2] = int(input('прибыль за 3 квартал предприятия: '))
  income[3] = int(input('прибыль за 4 квартал предприятия: '))
  s += sum(income)
  res[name] = sum(income)#отдельно сохраняем прибыль за год
  #print(income)
  #print(name)
  #print(sum(income))
  #print(collections.namedtuple(name, income))
#print(dict(zip(name,income)))
  Business[name] = income
#s += income
avrg = s / number
#print(Business)
#print(res)
#print(name)
print("\nСредняя прибыль за год: %.0f. Предприятия, чья прибыль выше среднего:" % avrg)
for key, value in res.items():
    if value > avrg:
        print(key)
print("Предприятия, чья прибыль ниже среднего: ")
for key, value in res.items():
    if value < avrg:
        print(key)
