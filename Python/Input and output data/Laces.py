# Обувная фабрика собирается начать выпуск элитной модели ботинок.
# Дырочки для шнуровки будут расположены в два столбца,
# расстояние между столбцами равно a, а расстояние между дырочками в столбце b.
# Количество дырочек в каждом столбце равно N.
# Шнуровка должна происходить элитным способом “наверх, по горизонтали
# в другой столбец, наверх, по горизонтали и т.д.”.
# Кроме того, чтобы шнурки можно было завязать элитным бантиком,
# длина свободного конца шнурка должна быть l.
# Какова должна быть длина шнурка для этих ботинок?
# Программа получает на вход четыре натуральных числа: a, b, l и N 
# и должна вывести одно число - искомую длину шнурка. 

# Shoe factory is going to start producing a luxury model of shoes.
# The holes for lacing will be located in two columns,
# the column spacing is a, and the distance between the holes in column b.
# The number of holes in each column equal to N.
# Lace-up must occur the elite way “upward, horizontally
# to another column, upward, horizontally, etc.”
# In addition to laces could tie elite bow,
# the length of the free end of the cord l.
# What should be the length of the lace for these boots?
# The program receives input four positive integers: a, b, l and N,
# and should print a single number - the desired length of the lace.

print('Обувная фабрика собирается начать выпуск элитной модели ботинок.')
print('Дырочки для шнуровки будут расположены в два столбца,')
print('расстояние между столбцами равно a, а расстояние между дырочками в столбце b.')
print('Количество дырочек в каждом столбце равно N.')
print('Шнуровка должна происходить элитным способом “наверх, по горизонтали')
print('в другой столбец, наверх, по горизонтали и т.д.”.')
print('Кроме того, чтобы шнурки можно было завязать элитным бантиком,')
print('длина свободного конца шнурка должна быть l.')
print('Какова должна быть длина шнурка для этих ботинок?')
print('Программа получает на вход четыре натуральных числа: a, b, l и N ')
print('и должна вывести одно число - искомую длину шнурка.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('Расстояние между столбцами: '))
    b = int(input('Расстояние между дырочками: '))
    l = int(input('Количество дырочек в столбце: '))
    N = int(input('Длина свободного конца шнурка: '))
    print('Длина шнурка = ' + str(a * (2 * N - 1) + 2 * b * (N - 1) + 2 * l))
    ans = input('Еще раз? y/n ')
