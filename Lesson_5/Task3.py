# Создайте программу для игры в ""Крестики-нолики"".


print('Введите желаемый размер поля для игры')
columns = int(input('Количество столбцов: '))
rows = int(input('Количество строк: '))
matrix = []
for i in range(rows):
    matrix.append([''] * columns)
size = columns * rows
player = 1
l = 0
while size != l:
    print ('Ход делает игрок №',player)
    print('Введите строку и стобец, куда хотите сделать ход: ')
    row = int(input('Строка: '))
    col = int(input('Столбец: '))
    if (row >= rows) or (col >= columns):
        print('Ошибка! Такой клетки нет. Попробуйте снова')
    elif (matrix[row][col] == 0) or (matrix[row][col] == 1):
        print('Эта клетка уже занята. Попробуйте снова')
        continue
    else:
        if player == 1:
            matrix[row][col] = 0
            player = 2
        else:
            matrix[row][col] = 1
            player = 1
        l += 1
    print(matrix)
check = False
for i in range(rows):
    for j in range(columns - 1):
        if matrix[i][j] == matrix[i][j + 1]:
            check = True
            k = matrix[i][j]
        else:
            check = False
            k = -1
    if check == True:
        break
if check == True:
    print('Победитель - игрок №', k + 1)
else:
    for i in range(columns):
        for j in range(rows - 1):
            if matrix[i][j] == matrix[i][j + 1]:
                check = True
                k = matrix[i][j]
            else:
                check = False
                k = -1
        if check == True:
            break
    if check == True:
        print('Победитель - игрок №', k + 1)
    else:
        print('Ничья!')


