# Дано натуральное число. Найдите число десятков в его десятичной записи.

# Given natural number. Find the number of tens in its decimal representation.

print('Дано натуральное число. Найти число десятков в его десятичной записи.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('a = '))
    print('В числе ' + str((a // 10) % 10) + ' десятков')
    ans = input('Еще раз? y/n ')
