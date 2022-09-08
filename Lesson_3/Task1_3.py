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
for k in range(len(array)):
    array[k] = round(array[k] % 1,2)
max = min = array[0]
for j in range(len(array)):
    if array[j] > max:
        max = array[j]
    else:
        if array[j] < min:
            min = array[j]
result =round((max - min), 2)
print('Разница между максимальной',max,'и минимальной',min,'дробными частями =',result)

