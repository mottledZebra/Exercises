# По российский правилам числа округляются до ближайшего целого числа,
# а если дробная часть числа равна 0.5, то число округляется вверх.
# Дано неотрицательное число x, округлите его по этим правилам.
# Обратите внимание, что функция round не годится для этой задачи!    

# According to Russian rules numbers are rounded to the nearest integer
# and if the fractional part of the number is 0.5, the number is rounded up.
# Given a nonnegative number x, round it by these rules.
# Please note that the ROUND function is not suitable for this task!

print('По российский правилам числа округляются до ближайшего целого числа,')
print('а если дробная часть числа равна 0.5, то число округляется вверх.')
print('Дано неотрицательное число x, округлить его по этим правилам.')
print()

import math

ans = 'y'

while ans == 'y':
    x = float(input('x = '))
    if (x - int(x)) >= 0.5:
        print(math.ceil(x))
    else:
        print(math.floor(x))
    ans = input('Еще раз? y/n ')
