# Напишите программу, которая считывает длины двух катетов
# в прямоугольном треугольнике и выводит его площадь.
# Каждое число записано в отдельной строке. 

# Write a program that reads the lengths of two sides
# in a right triangle and displays its area.
# Each number is written in a separate line.

print('Площадь прямоугольного треугольника')
print()

ans = 'y'

while ans == 'y':
    a = int(input('Первый катет = '))
    b = int(input('Второй катет = '))
    s = a * b / 2
    print('Площадь = ' + str(s))
    ans = input('Еще раз? y/n ')
