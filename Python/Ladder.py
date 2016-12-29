# По данному натуральному n ≤ 9 выведите лесенку из n ступенек,
# i-я ступенька состоит из чисел от 1 до i без пробелов. 

# For a given positive integer n ≤ 9, output a ladder of n steps,
# the I-th step consists of the numbers from 1 to i without spaces.

print('По данному натуральному n ≤ 9 вывести лесенку из n ступенек,')
print('i-я ступенька состоит из чисел от 1 до i без пробелов.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    for i in range(1, n + 1):
        s = ''
        for j in range(1, i + 1):
            s += str(j)
        print(s)
    ans = input('Еще раз? y/n ')
