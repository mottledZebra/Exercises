# Программа получает на вход последовательность целых неотрицательных чисел,
# каждое число записано в отдельной строке.
# Последовательность завершается числом 0,
# при считывании которого программа должна закончить свою работу
# и вывести количество элементов последовательности, которые больше предыдущих.
# Числа, следующие за числом 0, считывать не нужно.  

# The program takes on input a sequence of non-negative integers,
# each number is written in a separate line.
# The sequence ends with the number 0,
# when reading which the program should finish its work
# and bring the number of elements in the sequence that is greater than the previous.
# The number following the number with a 0, read is not necessary.

print('Программа получает на вход последовательность целых неотрицательных чисел,')
print('каждое число записано в отдельной строке.')
print('Последовательность завершается числом 0,')
print('при считывании которого программа должна закончить свою работу')
print('и вывести количество элементов последовательности, которые больше предыдущих.')
print()

ans = 'y'

while ans == 'y':
    k = i = 0
    n1 = int(input('a0 = '))
    while n1 != 0:
        i += 1
        n2 = int(input('a' + str(i) + ' = '))
        if n2 > n1:
            k += 1
        n1 = n2
    print(k)
    ans = input('Еще раз? y/n ')
