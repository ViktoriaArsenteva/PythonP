# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randint


array = []
size = randint(2,10)
for i in range(size):
    array.append(randint(0,100))
result = []
halfsize = size // 2
for i in range(halfsize):
    result.append(array[i] * array[-i-1])
if size % 2 != 0:
    result.append(array[halfsize] ** 2)
print('Исходный список: ',array)
print('Произведения пар чисел данного списка =',result)