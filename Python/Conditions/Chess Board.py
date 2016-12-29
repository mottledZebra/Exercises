# Заданы две клетки шахматной доски.
# Если они покрашены в один цвет, то выведите слово YES,
# а если в разные цвета — то NO.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки.

# Given two squares of the chessboard.
# If they are painted in one color, print the word YES,
# and if in different colors — NO.
# The program receives input four numbers from 1 to 8 each,
# that specify the column number and line number first for the first cell,
# then second cell.

print('Заданы две клетки шахматной доски.')
print('Если они покрашены в один цвет, то вывести слово YES,')
print('а если в разные цвета — то NO.')
print('Программа получает на вход четыре числа от 1 до 8 каждое,')
print('задающие номер столбца и номер строки сначала для первой клетки,')
print('потом для второй клетки.')
print()

ans = 'y'

while ans == 'y':
    a1 = int(input('№ столбца первой клетки: '))
    b1 = int(input('№ строки первой клетки: '))
    a2 = int(input('№ столбца второй клетки: '))
    b2 = int(input('№ строки второй клетки: '))
    if (a1 + b1) % 2 == 0 and (a2 + b2) % 2 == 0\
    or (a1 + b1) % 2 != 0 and (a2 + b2) % 2 != 0:
        print('YES')
    else:
        print('NO')
    ans = input('Еще раз? y/n ')
