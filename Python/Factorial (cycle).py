# Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.
# По данному натуральному n вычислите значение n!.
# Пользоваться математической библиотекой math в этой задаче запрещено. 

# The factorial of n is the product 1 × 2 × ... × n. Symbol: n!.
# For a given positive integer n, calculate the value of n!.
# To use the math library in this problem is prohibited.

print('Факториалом числа n называется произведение 1 × 2 × ... × n. Обозначение: n!.')
print('По данному натуральному n вычислить значение n!.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('n = '))
    p = 1
    for i in range(1, n + 1):
        p *= i
    print('n! = ' + str(p))
    ans = input('Еще раз? y/n ')
