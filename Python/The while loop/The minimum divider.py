# Дано целое число, не меньшее 2.
# Выведите его наименьший натуральный делитель, отличный от 1.

# Given an integer not less than 2.
# Output his smallest natural divisor other than 1.

print('Дано целое число, не меньшее 2.')
print('Вывести его наименьший натуральный делитель, отличный от 1.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    i = 2
    while i <= n:
        if n % i == 0:
            print(i)
            break
        i += 1
    ans = input('Еще раз? y/n ')
