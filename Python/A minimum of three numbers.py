# Даны три целых числа. Выведите значение наименьшего из них. 

# Given three integers. Print the smallest of them.

print('Даны три целых числа. Вывести значение наименьшего из них.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    print('Наименьшее число =', end = ' ')
    if a <= b and a <= c:
        print(str(a) + ' (a)')
    elif b <= a and b <= c:
        print(str(b) + ' (b)')
    else:
        print(str(c) + ' (c)')
    ans = input('Еще раз? y/n ')
