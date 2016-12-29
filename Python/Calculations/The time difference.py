# Даны значения двух моментов времени, принадлежащих одним и тем же суткам:
# часы, минуты и секунды для каждого из моментов времени.
# Известно, что второй момент времени наступил не раньше первого.
# Определите, сколько секунд прошло между двумя моментами времени.
# Программа на вход получает три целых числа:
# часы, минуты, секунды, задающие первый момент времени и три целых числа,
# задающих второй момент времени.
# Выведите число секунд между этими моментами времени.

# Given value at two points in time that belong to the same day:
# hours, minutes, and seconds for each of the time points.
# It is known that the second time occurred not before the first.
# Determine how many seconds have passed between two points in time.
# The program receives three integers:
# hours, minutes, seconds that specifies the first point in time and three integers
# that specify the second point in time.
# Print the number of seconds between these points in time.

print('Даны значения двух моментов времени, принадлежащих одним и тем же суткам:')
print('часы, минуты и секунды для каждого из моментов времени.')
print('Известно, что второй момент времени наступил не раньше первого.')
print('Определите, сколько секунд прошло между двумя моментами времени.')
print('Программа на вход получает три целых числа:')
print('часы, минуты, секунды, задающие первый момент времени и три целых числа,')
print('задающих второй момент времени.')
print('Вывести число секунд между этими моментами времени.')
print()

ans = 'y'

while ans == 'y':
    print('Первый момент:')
    h1 = int(input('часы: '))
    m1 = int(input('минуты: '))
    s1 = int(input('секунды: '))
    print('Второй момент:')
    h2 = int(input('часы: '))
    m2 = int(input('минуты: '))
    s2 = int(input('секунды: '))
    print('Между двумя моментами ' + str((h2 - h1) * 3600 + \
          + (m2 - m1) * 60 + (s2 - s1)) + ' секунд')
    ans = input('Еще раз? y/n ')
