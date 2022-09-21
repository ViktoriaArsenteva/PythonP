# Напишите программу, удаляющую из текста все слова, содержащие ""абв"".


text = open('fileforTask1.txt').read().split(' ')

j = 0
for i in range(len(text)):
    if text[j].lower().find('абв') != -1:
        text.pop(j)
        j -= 1
    j += 1

result = ''
for k in text:
    result += k + " "
file = open('resultFromTask1.txt','w').write(result)


