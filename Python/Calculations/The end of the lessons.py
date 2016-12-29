# В некоторой школе занятия начинаются в 9:00.
# Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д.
# уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.
# Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.
# Выведите два целых числа: время окончания урока в часах и минутах.

# In some school classes begin at 9:00.
# Lesson duration 45 minutes, after the 1st, 3rd, 5th, etc.
# lessons change in 5 minutes, and after the 2nd, 4th, 6th, etc — 15 minutes.
# Given a lesson (a number from 1 to 10). Determine when the end of the specified lesson.
# Print two integers: the end time of the lesson in hours and minutes.

print('В некоторой школе занятия начинаются в 9:00.')
print('Продолжительность урока — 45 минут, после 1-го, 3-го, 5-го и т.д.')
print('уроков перемена 5 минут, а после 2-го, 4-го, 6-го и т.д. — 15 минут.')
print('Дан номер урока (число от 1 до 10). Определите, когда заканчивается указанный урок.')
print('Выведите два целых числа: время окончания урока в часах и минутах.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('n = '))
    min = n // 2 * 110 + n % 2 * 45 + (n % 2 - 1) * 15
    print('Урок закончится в ' + str(min // 60 + 9) + \
          ' часов ' + str(min % 60) + ' минут')
    ans = input('Еще раз? y/n ')
