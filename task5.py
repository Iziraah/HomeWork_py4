# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

with open('FirstFile.txt', 'w') as file:
    file.write('56 78 12 95')
with open('SecondFile.txt', 'w') as file:
    file.write('89 45 36 74')
with open("Firstfile.txt") as file:
    firstPolyn = list(map(int, file.read().split()))
    print(firstPolyn)
with open("SecondFile.txt") as file:
    secondPolyn = list(map(int, file.read().split()))
    print(secondPolyn)
result = []
for i in range(4):
    res = firstPolyn[i] + secondPolyn[i]
    result.append(res)
resultStr = ' '.join(map(str, result))
with open('ResultFile.txt', 'w') as file:
    file.write(resultStr)



