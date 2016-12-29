# Шахматный король ходит по горизонтали, вертикали и диагонали,
# но только на 1 клетку.
# Даны две различные клетки шахматной доски, определите,
# может ли король попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести YES,
# если из первой клетки ходом короля можно попасть во вторую
# или NO в противном случае.  

# Chess king moves horizontally, vertically and diagonally
# but only 1 square.
# Given two different squares of the chessboard, determine
# whether a king to get from the first cell to the second one.
# The program receives input four numbers from 1 to 8 each,
# that specify the column number and line number first for the first cell,
# then second cell. The program should print YES
# if cell from the first move of the king can get to the second
# or NO otherwise.

print('Шахматный король ходит по горизонтали, вертикали и диагонали,')
print('но только на 1 клетку.')
print('Даны две различные клетки шахматной доски, определите,')
print('может ли король попасть с первой клетки на вторую одним ходом.')
print('Программа получает на вход четыре числа от 1 до 8 каждое,')
print('задающие номер столбца и номер строки сначала для первой клетки,')
print('потом для второй клетки. Программа должна вывести YES,')
print('если из первой клетки ходом короля можно попасть во вторую')
print('или NO в противном случае.')
print()

ans = 'y'

while ans == 'y':
    x1 = int(input('№ столбца первой клетки: '))
    y1 = int(input('№ строки первой клетки: '))
    x2 = int(input('№ столбца второй клетки: '))
    y2 = int(input('№ строки второй клетки: '))
    if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
        print('YES')
    else:
        print('NO')
    ans = input('Еще раз? y/n ')
