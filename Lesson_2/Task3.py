# Реализуйте алгоритм перемешивания списка.

from random import randint
 
num = randint(10,100)
array = []
for i in range(num):
    array.append(i)
print(array)
for f in range(2,5):
    for j in range (0,num,f):
        for k in range(num):
            array[j],array[k] = array[k],array[j]
print(array)