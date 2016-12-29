# Дано число n. С начала суток прошло n минут.
# Определите, сколько часов и минут будут показывать
# электронные часы в этот момент.
# Программа должна вывести два числа: количество часов (от 0 до 23)
# и количество минут (от 0 до 59).
# Учтите, что число n может быть больше, чем количество минут в сутках. 

# The given number n. Since the beginning of days passed n minutes.
# Determine how many hours and minutes will show
# a digital watch at this point.
# The program should print two numbers: the number of hours (0 to 23)
# and minutes (0 to 59).
# Note that n can be greater than the number of minutes in a day.

print('Дано число n. С начала суток прошло n минут.')
print('Определите, сколько часов и минут будут показывать ')
print('электронные часы в этот момент.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('n = '))
    h = n // 60
    h = h % 24
    m = n % 60
    print('С начала суток прошло ' + str(h) + ' часов, ' + str(m) + ' минут')
    ans = input('Еще раз? y/n ')
