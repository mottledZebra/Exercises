# Напишите программу, которая считывает целое число и выводит
# следующее за ним и предыдущее значение.

# Write a program that reads an integer and displays
# the next and previous value.

print('Напишите программу, которая считывает целое число и выводит')
print('следующее за ним и предыдущее значение.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('n = '))
    print('Следующее число после числа ' +
        str(n) + ' это ' + str(n + 1))
    print('Предыдущее число перед числом ' +
        str(n) + ' это ' + str(n - 1))
    ans = input('Еще раз? y/n ')
