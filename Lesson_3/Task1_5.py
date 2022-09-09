# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

num = int(input('Введите число для создания списка чисел Фибоначчи: '))
result = []

def Fibonacci(num):
    fib = [0, 1]
    i = num - 1
    for j in range(i):
        fib.append(fib[j] + fib[j + 1])
    minusfib = []
    for k in range(len(fib) - 1):
        if num % 2 == 0:
            if k % 2 == 0:
                minusfib.append(-fib[-k-1]) 
            else:
                minusfib.append(fib[-k-1])
        else:
            if k % 2 == 0:
                minusfib.append(fib[-k-1]) 
            else:
                minusfib.append(-fib[-k-1])
    fibonacci = minusfib + fib
    return fibonacci
    
print(Fibonacci(num))
