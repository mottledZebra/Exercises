# Процентная ставка по вкладу составляет P процентов годовых,
# которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.
# Определите размер вклада через год.
# Программа получает на вход целые числа P, X, Y и должна вывести два числа:
# величину вклада через год в рублях и копейках.
# Дробная часть копеек отбрасывается.      

# Interest rate on Deposit is P percent per annum,
# which is added to the Deposit amount. The contribution is X rubles Y kopecks.
# Determine the size of the investment in a year.
# The program receives the input of the integers P, X, Y, and should output two numbers:
# the amount of contribution in a year in rubles and kopecks.
# The fractional part kopecks is discarded .

print('Процентная ставка по вкладу составляет P процентов годовых,')
print('которые прибавляются к сумме вклада. Вклад составляет X рублей Y копеек.')
print('Определить размер вклада через год.')
print('Программа получает на вход целые числа P, X, Y и должна вывести два числа:')
print('величину вклада через год в рублях и копейках.')
print('Дробная часть копеек отбрасывается.')
print()

import math

ans = 'y'

while ans == 'y':
    p = int(input('Процентная ставка, % годовых: '))
    x = int(input('Вклад, рублей: '))
    y = int(input('       копеек: '))
    y1 = (x * 100 + y)*(100 + p) / 100
    x1 = y1 // 100
    y2 = y1 % 100
    print('Размер вклада через год: ' + str(int(x1)) + ' руб ' + str(int(y2)) + ' коп')
    ans = input('Еще раз? y/n ')
