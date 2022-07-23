#Задайте последовательность чисел. 
#Напишите программу, которая выведет список неповторяющихся элементов исходной 
#последовательности.

num = list(map(int, input('Введите последовательность чисел через пробел: ').split()))

def UniqNum(num):
    uniq = []
    for number in num:
        if number in uniq:
            continue
        else:
            uniq.append(number)
    return uniq

print('Неповторяющиеся элементы исходной последовательности: ', UniqNum(num))