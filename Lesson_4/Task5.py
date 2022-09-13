# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

f1 = open('File1.txt').read()
f2 = open('File2.txt').read()
k1 = int(f1[f1.find('*') - 2]) + int(f2[f2.find('*') - 2]) 
k2 = int(f1[f1.find('+') + 2]) + int(f2[f2.find('+') + 2])
k3 = int(f1[f1.find('=') - 2]) + int(f2[f2.find('=') - 2])
f1 = f1[:f1.find('*') - 2] + str(k1) + f1[f1.find('*') - 1:]
f1 = f1[:f1.find('+') + 2] + str(k2) + f2[f2.find('+') + 3:]
f1 = f1[:f1.find('=') - 2] + str(k3) + f2[f2.find('=') - 1:]
file = open('Result.txt','w').write(f1)

