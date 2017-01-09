# В первый день спортсмен пробежал X километров,
# а затем он каждый день увеличивал пробег на 10% от предыдущего значения.
# По данному числу Y определите номер дня, на который пробег спортсмена
# составит не менее Y километров.
# Программа получает на вход действительные числа X и Y и должна вывести
# одно натуральное число. 

# On the first day of the athlete ran X miles
# and then every day he increased the mileage by 10% from the previous value.
# On this number Y determine the number of the day to which the mileage of the athlete
# is not less than Y miles.
# The program takes on input a real number X and Y, and should output
# a single integer.

print('В первый день спортсмен пробежал X километров,')
print('а затем он каждый день увеличивал пробег на 10% от предыдущего значения.')
print('По данному числу Y определить номер дня, на который пробег спортсмена')
print('составит не менее Y километров.')
print()

ans = 'y'

while ans == 'y':
    x = int(input('X = '))
    y = int(input('Y = '))
    i = 1
    while x < y:
        x *= 1.1
        i += 1
    print(i)
    ans = input('Еще раз? y/n ')
