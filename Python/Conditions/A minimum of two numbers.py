# Даны два целых числа. Выведите значение наименьшего из них. 

# Given two integers. Print the smallest of them.

print('Даны два целых числа. Вывести значение наименьшего из них.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('a = '))
    b = int(input('b = '))
    print('Наименьшее число =', end = ' ')
    if a < b:
        print(str(a) + ' (a)')
    else:
        print(str(b) + ' (b)')
    ans = input('Еще раз? y/n ')
