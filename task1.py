# Вычислить число pi c заданной точностью d Пример:
# - при d = 0.001, π = 3.141.    10^{-1} ≤ d ≤10^{-10}


import math
from math import factorial as fact

i, sgn = 1, -1
a, b, c = 13591409, 545140134, 640320
d = c ** (3/2)
s = a / d 
pi = 3
while str(pi)[:12] != '3.1415926535' :
    tmp = (sgn * fact(6*i) * (a + b*i) / 
    (fact(3*i) * fact(i) ** 3 * d * c**(3*i)))
    s += tmp
    sgn *= -1
    pi = 1 / (12*s)

f = float(input('Введите значение d от 0,1 до 0,0000000001: '))
count = 0
while f !=1:
    f = f * 10
    count +=1

d = count

print(round(pi,d))