# Дано трехзначное число. Найдите сумму его цифр.

# Given three-digit number. Find the sum of its digits.

print('Дано трехзначное число. Найти сумму его цифр.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('a = '))
    print('Сумма цифр ' + str((a // 100) % 100 + (a // 10) % 10 + a % 10))
    ans = input('Еще раз? y/n ')
