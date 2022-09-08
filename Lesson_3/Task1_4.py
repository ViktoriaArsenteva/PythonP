# Напишите программу, которая будет преобразовывать десятичное число в двоичное (без встроенных функций).
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10


number = num = int(input('Введите десятичное число: '))
decimal = []
while number >= 2:
    decimal.append(number % 2)
    number //= 2
if num != 0:
    decimal.append(1)
else:
    decimal.append(0)
decimal.reverse()
result = ''
for i in range(len(decimal)):
    result = result + str(decimal[i])
    i += 1
print('Десятичное число',num,'в двоичной системе счисления =',result)