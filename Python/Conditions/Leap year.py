# Дано натуральное число. Требуется определить, является ли год
# с данным номером високосным. Если год является високосным,
# то выведите YES, иначе выведите NO.
# Напомним, что в соответствии с григорианским календарем,
# год является високосным, если его номер кратен 4, но не кратен 100,
# а также если он кратен 400. 

# Given natural number. You must to determine whether
# leap year a year with this number. If the year is a leap year,
# print YES, otherwise print NO.
# Recall that, in accordance with the Gregorian calendar,
# a year is a leap year if its number is a multiple of 4 but not multiple of 100,
# and if it is multiple of 400.

print('Дано натуральное число. Требуется определить, является ли год')
print('с данным номером високосным. Если год является високосным,')
print('то вывести YES, иначе вывести NO.')
print('Напомним, что в соответствии с григорианским календарем,')
print('год является високосным, если его номер кратен 4, но не кратен 100,')
print('а также если он кратен 400.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('год = '))
    if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
        print('YES')
    else:
        print('NO')
    ans = input('Еще раз? y/n ')
