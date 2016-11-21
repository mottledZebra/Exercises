# За день машина проезжает N километров.
# Сколько дней нужно, чтобы проехать маршрут длиной M километров?
# Программа получает на вход числа N и M.

# Car of the day passes N kilometers.
# How many days need to follow the route of length M kilometers?
# The program takes on input the numbers N and M.

print('За день машина проезжает N километров.')
print('Сколько дней нужно, чтобы проехать маршрут длиной M километров?')
print('Программа получает на вход числа N и M.')
print()

ans = 'y'

while ans == 'y':
    import math
    N = int(input('N = '))
    M = int(input('M = '))
    print(str(math.ceil(M / N)) + ' дней')
    ans = input('Еще раз? y/n ')
