# Шахматный конь ходит буквой “Г” — на две клетки по вертикали
# в любом направлении и на одну клетку по горизонтали, или наоборот. 
# Даны две различные клетки шахматной доски, определите,
# может ли слон попасть с первой клетки на вторую одним ходом.
# Программа получает на вход четыре числа от 1 до 8 каждое,
# задающие номер столбца и номер строки сначала для первой клетки,
# потом для второй клетки. Программа должна вывести YES,
# если из первой клетки ходом слона можно попасть во вторую
# или NO в противном случае.  

# Chess horse moves two squares vertically
# in any direction and one square horizontally, or vice versa.
# Given two different squares of the chessboard, determine
# whether a horse to get from the first cell to the second one.
# The program receives input four numbers from 1 to 8 each,
# that specify the column number and line number first for the first cell,
# then second cell. The program should print YES
# if cell from the first move of the horse can get to the second
# or NO otherwise.

print('Шахматный конь ходит буквой “Г” — на две клетки по вертикали')
print('в любом направлении и на одну клетку по горизонтали, или наоборот.')
print('Даны две различные клетки шахматной доски, определите,')
print('может ли конь попасть с первой клетки на вторую одним ходом.')
print('Программа получает на вход четыре числа от 1 до 8 каждое,')
print('задающие номер столбца и номер строки сначала для первой клетки,')
print('потом для второй клетки. Программа должна вывести YES,')
print('если из первой клетки ходом коня можно попасть во вторую')
print('или NO в противном случае.')
print()

ans = 'y'

while ans == 'y':
    x1 = int(input('№ столбца первой клетки: '))
    y1 = int(input('№ строки первой клетки: '))
    x2 = int(input('№ столбца второй клетки: '))
    y2 = int(input('№ строки второй клетки: '))
    s1 = x1 + y1
    s2 = x2 + y2
    if x1 != x2 and y1 != y2 and (abs(s1 - s2) == 3 or abs(s1 - s2) == 1):
        print('YES')
    else:
        print('NO')
    ans = input('Еще раз? y/n ')
