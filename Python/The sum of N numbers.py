# Дано несколько чисел. Вычислите их сумму.
# Сначала вводите количество чисел N, затем вводится ровно N целых чисел.
# Какое наименьшее число переменных нужно для решения этой задачи?   

# Given a few numbers. Calculate their sum.
# First enter the number of integers N, then enter exactly N integers.
# What is the smallest number of variables needed to solve this problem?

print('Дано несколько чисел. Вычислить их сумму.')
print('Сначала вводится количество чисел N, затем вводится ровно N целых чисел.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    s = 0
    for i in range(0, n):
        s += int(input('a' + str(i + 1) + ' = '))
    print(s)
    ans = input('Еще раз? y/n ')
