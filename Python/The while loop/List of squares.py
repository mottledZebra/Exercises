# По данному целому числу N распечатайте все квадраты натуральных чисел,
# не превосходящие N, в порядке возрастания.

# For a given integer N, print all the squares of natural numbers
# not exceeding N, in ascending order.

print('По данному целому числу N распечать все квадраты натуральных чисел,')
print('не превосходящие N, в порядке возрастания.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    i = 1
    while (i ** 2) <= n:
        print(i ** 2)
        i += 1
    ans = input('Еще раз? y/n ')
