# Программа получает на вход последовательность целых неотрицательных чисел,
# каждое число записано в отдельной строке.
# Последовательность завершается числом 0,
# при считывании которого программа должна закончить свою работу
# и вывести количество четных элементов последовательности.
# Числа, следующие за числом 0, считывать не нужно.  

# The program takes on input a sequence of non-negative integers,
# each number is written in a separate line.
# The sequence ends with the number 0,
# when reading which the program should finish its work
# and bring the number of odd elements of the sequence.
# The number following the number with a 0, read is not necessary.

print('Программа получает на вход последовательность целых неотрицательных чисел,')
print('каждое число записано в отдельной строке.')
print('Последовательность завершается числом 0,')
print('при считывании которого программа должна закончить свою работу')
print('и вывести количество четных элементов последовательности.')
print()

ans = 'y'

while ans == 'y':
    k = i = 0
    n = int(input('a0 = '))
    while n != 0:
        if n % 2 == 0:
            k += 1
        i += 1
        n = int(input('a' + str(i) + ' = '))
    print(k)
    ans = input('Еще раз? y/n ')
