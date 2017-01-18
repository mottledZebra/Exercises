# Программа получает на вход последовательность целых неотрицательных чисел,
# каждое число записано в отдельной строке.
# Последовательность завершается числом 0,
# при считывании которого программа должна закончить свою работу
# и вывести значение наибольшего элемента последовательности.
# Числа, следующие за числом 0, считывать не нужно.  

# The program takes on input a sequence of non-negative integers,
# each number is written in a separate line.
# The sequence ends with the number 0,
# when reading which the program should finish its work
# and bring the value of the largest element of the sequence.
# The number following the number with a 0, read is not necessary.

print('Программа получает на вход последовательность целых неотрицательных чисел,')
print('каждое число записано в отдельной строке.')
print('Последовательность завершается числом 0,')
print('при считывании которого программа должна закончить свою работу')
print('и вывести значение наибольшего элемента последовательности.')
print()

ans = 'y'

while ans == 'y':
    i = 0
    max = n = int(input('a1 = '))
    while n != 0:
        if n > max:
            max = n
        i += 1
        n = int(input('a' + str(i + 1) + ' = '))
    print(max)
    ans = input('Еще раз? y/n ')
