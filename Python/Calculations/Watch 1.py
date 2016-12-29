# С начала суток прошло H часов, M минут, S секунд
# (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
# По данным числам H, M, S определите угол (в градусах),
# на который повернулаcь часовая стрелка с начала суток
# и выведите его в виде действительного числа.    

# Since the beginning of days it took H hours, M minutes, S seconds
# (0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).
# According to the numbers H, M, S, determine the angle (in degrees)
# that turned the hour hand with the beginning of the day
# and print it in the form of real numbers.

print('С начала суток прошло H часов, M минут, S секунд')
print('(0 ≤ H < 12, 0 ≤ M < 60, 0 ≤ S < 60).')
print('По данным числам H, M, S определить угол (в градусах),')
print('на который повернулаcь часовая стрелка с начала суток')
print('и вывести его в виде действительного числа.')
print()

import math

ans = 'y'

while ans == 'y':
    h = int(input('H = '))
    m = int(input('M = '))
    s = int(input('S = '))
    print('Часовая стрелка повернулась на ' +\
          str((h * 60 * 60 + m * 60 + s) * 360 / 43200) + ' градусов')
    ans = input('Еще раз? y/n ')
