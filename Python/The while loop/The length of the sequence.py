# Программа получает на вход последовательность целых неотрицательных чисел,
# каждое число записано в отдельной строке.
# Последовательность завершается числом 0,
# при считывании которого программа должна закончить свою работу
# и вывести количество членов последовательности (не считая завершающего числа 0).
# Числа, следующие за числом 0, считывать не нужно.  

# The program takes on input a sequence of non-negative integers,
# each number is written in a separate line.
# The sequence ends with the number 0,
# when reading which the program should finish its work
# and bring the number of members of the sequence (not including the terminating number 0).
# The number following the number with a 0, read is not necessary.

print('Программа получает на вход последовательность целых неотрицательных чисел,')
print('каждое число записано в отдельной строке.')
print('Последовательность завершается числом 0,')
print('при считывании которого программа должна закончить свою работу')
print('и вывести количество членов последовательности (не считая завершающего числа 0).')
print()

ans = 'y'

while ans == 'y':
    i = 0
    while int(input('a' + str(i + 1) + ' = ')) != 0:
        i += 1
    print(i)
    ans = input('Еще раз? y/n ')
