# Дано 10 целых чисел. Вычислите их сумму.
# Напишите программу, использующую наименьшее число переменных.  

# Given 10 integers. Calculate their sum.
# Write a program that uses the smallest number of variables.

print('Дано 10 целых чисел. Вычислить их сумму.')
print()

ans = 'y'

while ans == 'y':
    s = 0
    for i in range(0, 10):
        s += int(input('a' + str(i + 1) + ' = '))
    print(s)
    ans = input('Еще раз? y/n ')
