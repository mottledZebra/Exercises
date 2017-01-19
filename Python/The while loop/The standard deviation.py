# Определите стандартное отклонение σ для данной последовательности
# натуральных чисел,завершающейся числом 0.  

# Determine the standard deviation σ for a given sequence
# of natural numbers ending with the number 0.

print('Определить стандартное отклонение для данной последовательности')
print('натуральных чисел,завершающейся числом 0.')
print()

ans = 'y'

while ans == 'y':
    x = input('a0 = ')
    m = ''
    n = 0
    s = 0
    t = 0
    while x != '0':
        m += x + ' '
        n += 1
        s += int(x)
        x = input('a' + str(n) + ' = ')
    s /= n
    for i in range(0, n):
        x = m[: m.find(' ')]
        m = m.replace(x + ' ', '', 1)
        t += (int(x) - s) ** 2
    t = (t / (n - 1)) ** 0.5
    print('σ = ' + str(t))
    ans = input('Еще раз? y/n ')
