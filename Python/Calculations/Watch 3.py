# С начала суток часовая стрелка повернулась на угол в α градусов.
# Определите сколько полных часов, минут и секунд прошло с начала суток,
# то есть решите задачу, обратную задаче «Часы - 1».
# Запишите ответ в три переменные и выведите их на экран.     

# Since the beginning of the day, the hour hand turned at an angle of α degrees.
# Determine how many total hours, minutes and seconds have passed since the beginning
# of the day, that is, solve the problem, the inverse problem of "Watch - 1".
# Write down the answer in three variables and print them to the screen.

print('С начала суток часовая стрелка повернулась на угол в α градусов.')
print('Определить сколько полных часов, минут и секунд прошло с начала суток,')
print('то есть решить задачу, обратную задаче «Часы - 1».')
print('Записать ответ в три переменные и вывести их на экран.')
print()

import math

ans = 'y'

while ans == 'y':
    a = float(input('a = '))
    h = a // 30
    m = (a % 30) * 12 // 6
    s = ((a % 30) * 12 % 6) * 10
    print('С начала суток прошло ' + str(int(h)) + ' часов '\
          + str(int(m)) + ' минут ' + str(int(s)) + ' секунд')
    ans = input('Еще раз? y/n ')
