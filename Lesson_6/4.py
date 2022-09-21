# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу 
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 10.01] => 0.19

from random import randint, random, uniform

array = []
size = randint(2,10)
for i in range(size):
    array.append(round(uniform(0,100),2))
print('Исходный список:',array)
Newarray = lambda x: round(x % 1,2)
newarray = list(map(Newarray,array))
max = min = newarray[0]
for j in range(len(newarray)):
    if newarray[j] > max:
        max = newarray[j]
    else:
        if newarray[j] < min:
            min = newarray[j]
result =round((max - min), 2)
print('Разница между максимальной',max,'и минимальной',min,'дробными частями =',result)

