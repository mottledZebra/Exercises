# Яша плавал в бассейне размером N × M метров и устал.
# В этот момент он обнаружил, что находится на расстоянии
# x метров от одного из длинных бортиков (не обязательно от ближайшего)
# и y метров от одного из коротких бортиков.
# Какое минимальное расстояние должен проплыть Яша,
# чтобы выбраться из бассейна на бортик?
# Программа получает на вход числа N, M, x, y.
# Программа должна вывести число метров, которое нужно проплыть Яше до бортика.    

# Yasha swam in a pool of size N × M meters and tired.
# In this moment he found that is at a distance
# x meters from one of the long sides (not necessarily the nearest)
# and y meters from one of the short sides.
# What is the minimum distance to sail Yasha
# to get out of the pool to the skirting?
# The program takes on input the numbers N, M, x, y.
# The program should print the number of meters that need Yasha to swim to the skirting.

print('Яша плавал в бассейне размером N × M метров и устал.')
print('В этот момент он обнаружил, что находится на расстоянии')
print('x метров от одного из длинных бортиков (не обязательно от ближайшего)')
print('и y метров от одного из коротких бортиков.')
print('Какое минимальное расстояние должен проплыть Яша,')
print('чтобы выбраться из бассейна на бортик?')
print('Программа получает на вход числа N, M, x, y.')
print('Программа должна вывести число метров, которое нужно проплыть Яше до бортика.')
print()

ans = 'y'

while ans == 'y':
    N = int(input('N = '))
    M = int(input('M = '))
    x = int(input('x = '))
    y = int(input('y = '))
    if N > M:
        a = M - x
        b = N - y
    else:
        a = N - x
        b = M - y
    min = x
    if y < min:
        min = y
    if a < min:
        min = a
    if b < min:
        min = b
    print(min)
    ans = input('Еще раз? y/n ')
