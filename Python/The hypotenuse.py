# Дано два числа a и b. Выведите гипотенузу треугольника с заданными катетами.

# Given two numbers A and B. Output the hypotenuse of the triangle with the given sides.

print('Дано два числа a и b. Вывести гипотенузу треугольника с заданными катетами.')
print()

import math

ans = 'y'

while ans == 'y':
    a = float(input('a = '))
    b = float(input('b = '))
    print('Гипотенуза ' + str(math.sqrt(a ** 2 + b ** 2)))
    ans = input('Еще раз? y/n ')
