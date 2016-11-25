# С начала суток часовая стрелка повернулась на угол в α градусов.
# Определите на какой угол повернулась минутная стрелка с начала последнего часа.
# Входные и выходные данные — действительные числа.     

# Since the beginning of the day, the hour hand turned at an angle of α degrees.
# Determine the angle turned the minute-hand since the beginning of the last hour.
# Input and output real numbers.

print('С начала суток часовая стрелка повернулась на угол в α градусов.')
print('Определить, на какой угол повернулась минутная стрелка с начала последнего часа.')
print('Входные и выходные данные — действительные числа.')
print()

import math

ans = 'y'

while ans == 'y':
    a = float(input('a = '))
    print('Минутная стрелка повернулась на ' + str((a % 30) * 12) + ' градусов')
    ans = input('Еще раз? y/n ')
