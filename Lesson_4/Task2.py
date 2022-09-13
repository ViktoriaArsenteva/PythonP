# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.
# "20" -> [2, 2, 5]

n = int(input('Введите число, для вывода его простых множителей: '))
numbers = [i for i in range(2,1000)]
primenumbers = []
for k in numbers:
    control = True
    for j in range (2,1000):
        if j == k:
            continue
        else:
            if k % j != 0:
                control = True
            else:
                control = False
                break
    if control == True:
        primenumbers.append(k)
print(primenumbers)
result = []
check = True
op = 1


        