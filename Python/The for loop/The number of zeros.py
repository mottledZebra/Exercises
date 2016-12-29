# Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.
# Подсчитайте количество нулей среди введенных чисел и выведите это количество.
# Вам нужно подсчитать количество чисел, равных нулю, а не количество цифр. 

# Given N numbers: first, enter the number N then enter exactly N integers.
# Count the number of zeros among the entered numbers and print this count.
# You need to count the number of numbers equal to zero and not the number of digits.

print('Дано N чисел: сначала вводится число N, затем вводится ровно N целых чисел.')
print('Подсчитать количество нулей среди введенных чисел и вывести это количество.')
print('Нужно подсчитать количество чисел, равных нулю, а не количество цифр.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    s = 0
    for i in range(0, n):
        if int(input('a' + str((i + 1)) + ' = ')) == 0:
            s += 1
    print('нулю равно ' + str(s) + ' чисел')
    ans = input('Еще раз? y/n ')
