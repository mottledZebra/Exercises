# По данному натуральному числу N найдите наибольшую целую степень двойки,
# не превосходящую N. Выведите показатель степени и саму степень.
# Операцией возведения в степень пользоваться нельзя!

# For a given natural number N find the greatest integer power of two,
# not superior to N. Output the exponent and the degree.
# Operation of exponentiation can not be used!

print('По данному натуральному числу N найти наибольшую целую степень двойки,')
print('не превосходящую N. Вывести показатель степени и саму степень.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    i = 0
    s = 1
    while s <= n:
        s *= 2
        i += 1
    print(i - 1, s // 2)
    ans = input('Еще раз? y/n ')
