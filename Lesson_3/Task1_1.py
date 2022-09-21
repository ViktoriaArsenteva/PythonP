# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных индексы элементы 3 и 9, ответ: 12

from random import randint

array = []
size = randint(2,10)
for i in range(size):
    array.append(randint(0,100))
summ = 0
index = 1
while index < len(array):
    summ += array[index]
    index += 2
print('Исходный список:',array)
print('Сумма элементов списка, стоящих на нечетной позиции =',summ)
