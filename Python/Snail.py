# Улитка ползет по вертикальному шесту высотой h метров,
# поднимаясь за день на a метров, а за ночь спускаясь на b метров.
# На какой день улитка доползет до вершины шеста?
# Программа получает на вход натуральные числа h, a, b.
# Программа должна вывести одно натуральное число.
# Гарантируется, что a>b. 

# Snail crawling on a vertical pole of height H metres of
# climbing per day on A meters, and during the night, going down to a B meters.
# On which day the snail crawls to the top of the pole?
# The program takes on input a natural number H, A, B.
# The program should output a single integer.
# It is guaranteed that A>B.

print('Улитка ползет по вертикальному шесту высотой h метров,')
print('поднимаясь за день на a метров, а за ночь спускаясь на b метров.')
print('На какой день улитка доползет до вершины шеста?')
print('Программа получает на вход натуральные числа h, a, b.')
print('Программа должна вывести одно натуральное число.')
print('Гарантируется, что a>b.')
print()

import math

ans = 'y'

while ans == 'y':
    h = int(input('h = '))
    a = int(input('a = '))
    b = int(input('b = '))
    print('Улитка доползет до вершины на ' + \
          str(math.ceil((h - a) / (a - b)) + 1) + ' день')
    ans = input('Еще раз? y/n ')
