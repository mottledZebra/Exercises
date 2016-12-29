# Дано положительное действительное число X. Выведите его дробную часть.

# Given a positive real number X. Output the fractional part.

print('Дано положительное действительное число X. Вывести его дробную часть.')
print()

ans = 'y'

while ans == 'y':
    a = float(input('a = '))
    print('Дробная часть ' + str(a - int(a)))
    ans = input('Еще раз? y/n ')
