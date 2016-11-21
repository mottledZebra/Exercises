# Дано положительное действительное число X.
# Выведите его первую цифру после десятичной точки. 

# Given a positive real number X.
# Outputting the first digit after the decimal point.

print('Дано положительное действительное число X.')
print('Вывести его первую цифру после десятичной точки.')
print()

ans = 'y'

while ans == 'y':
    a = float(input('a = '))
    print('Первая цифра после точки ' + str(int(a * 10) % 10))
    ans = input('Еще раз? y/n ')
