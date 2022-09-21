# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.

text = input()
count = 1
result = []
for i in range(len(text) - 1):
    if text[i] == text[i + 1]:
        count += 1
    else:
        result.append((text[i],count))
        count = 1
result.append((text[i+1],count))
print(result)

rehab = ''
for j in range(len(result)):
    rehab += result[j][0] * result[j][1]
print(rehab)

