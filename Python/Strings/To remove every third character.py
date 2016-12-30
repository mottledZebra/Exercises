# Дана строка. Удалите из нее все символы, чьи индексы делятся на 3.

# Given a string. Remove all symbols whose indices are divisible by 3.

print('Дана строка. Удалить из нее все символы, чьи индексы делятся на 3.')
print()

ans = 'y'

while ans == 'y':
    s = input('строка: ')
    s1 = s
    for i in range(0, len(s), 3):
        s1 = s1.replace(s[i :], '') + s[i + 1 :]
    print(s1)
    ans = input('Еще раз? y/n ')
