# Дано натуральное число. Выведите его последнюю цифру.

# Given natural number. Print its last digit.

print('Дано натуральное число. Вывести его последнюю цифру.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('a = '))
    print('Последняя цифра ' + str(a % 10))
    ans = input('Еще раз? y/n ')
