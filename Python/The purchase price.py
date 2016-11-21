# Пирожок в столовой стоит A рублей и B копеек.
# Определите, сколько рублей и копеек нужно заплатить за N пирожков.
# Программа получает на вход три числа: A, B, N,
# и должна вывести два числа: стоимость покупки в рублях и копейках.

# Pie in the dining room is A rubles and B kopecks.
# Determine how many rubles and kopecks to pay for N pies.
# The program takes on input three integers: a, b, n,
# and should print two numbers: the purchase price in roubles and kopecks.

print('Пирожок в столовой стоит a рублей и b копеек.')
print('Определите, сколько рублей и копеек нужно заплатить за n пирожков.')
print('Программа получает на вход три числа: a, b, n,')
print('и должна вывести два числа: стоимость покупки в рублях и копейках.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('a = '))
    b = int(input('b = '))
    n = int(input('n = '))
    print(str(a * n + (b * n) // 100) + ' руб ' + str((b * n) % 100) + ' коп')
    ans = input('Еще раз? y/n ')
