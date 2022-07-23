# Задана натуральная степень k. Сформировать случайным образом список коэффициентов 
# (значения от 0 до 100) многочлена и записать в файл многочлен степени k.
# Пример:k=2 =>
# 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

import random
n = int(input('Введите количество коэффициентов k: '))
arr = []
for i in range(n): arr.append(random.randint(0, 100))
print(arr)
indk = arr[int(input('Введите индекс коэффициента k: '))]
indk2 = str(indk)
my_file = open('NewFile.txt', 'w')
my_file.write('resulting polynomial is: ' + '\n')
my_file.write('2 * x ^ ')
my_file.write(indk2)
my_file.write(' + 4 * x + 5 = 0')
my_file.close()