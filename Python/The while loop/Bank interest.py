# Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,
# после чего дробная часть копеек отбрасывается.
# Определите, через сколько лет вклад составит не менее Y рублей. 
# Программа получает на вход три натуральных числа:
# X, P, Y и должна вывести одно целое число.  

# Bank deposit is X rubles. Annually it increases by P percent,
# after then the fractional part is discarded cents.
# Determine, how many years the contribution will be not less than Y rubles.
# The program receives the input of three integers:
# X, P, Y, and should output a single integer.

print('Вклад в банке составляет X рублей. Ежегодно он увеличивается на P процентов,')
print('после чего дробная часть копеек отбрасывается.')
print('Определить, через сколько лет вклад составит не менее Y рублей.')
print()

ans = 'y'

while ans == 'y':
    x = int(input('X = '))
    p = int(input('P = '))
    y = int(input('Y = '))
    i = 0
    while x < y:
        x *= (1 + p / 100)
        x = int(x * 100)
        x /= 100
        i += 1
    print(str(i) + ' лет')
    ans = input('Еще раз? y/n ')
