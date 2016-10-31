# Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают),
# 2 (если два совпадает) или 0 (если все числа различны). 

# Given three integers. Determine how many of them are coincident.
# Program should print one of the numbers: 3 (if all same),
# 2 (if two matches) or 0 (if all numbers are different).

print('Даны три целых числа. Определите, сколько среди них совпадающих.')
print('Программа должна вывести одно из чисел: 3 (если все совпадают),')
print('2 (если два совпадает) или 0 (если все числа различны).')
print()

ans = 'y'

while ans == 'y':
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    if a == b == c:
        print(3)
    elif a != b and a != c and b != c:
        print(0)
    else:
        print(2)
    ans = input('Еще раз? y/n ')
