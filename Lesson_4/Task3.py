# Задайте последовательность чисел. Напишите программу, которая выведет список 
# неповторяющихся элементов исходной последовательности.
# [1, 1, 2, 3, 4, 5, 5] -> [2, 3, 4]


list = input('Введите последовательность элементов через пробел: ').split( )
print(list)
result = []
for i in range(len(list)):
    check = False
    for j in range(len(list)):
        if i == j:
            continue
        if list[i] == list[j]:
            check = True
            break
    if check == False:
        result.append(list[i])
print('Неповторяющиеся элементы исходной последовательности:',result)

