# Дана строка. Замените в этой строке все цифры 1 на слово one.  

# Given a string. Replace in this string all the digits 1 to the word one.

print('Дана строка. Заменить в этой строке все цифры 1 на слово one.')
print()

ans = 'y'

while ans == 'y':
    print(input('строка: ').replace('1', 'one'))
    ans = input('Еще раз? y/n ')
