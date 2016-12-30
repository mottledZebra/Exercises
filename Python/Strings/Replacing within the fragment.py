# Дана строка. Замените в этой строке все появления буквы h на букву H,
# кроме первого и последнего вхождения.  

# Given a string. Replace in this line, all occurrence of the letter h to the letter H,
# except for the first and last occurrence.

print('Дана строка. Заменить в этой строке все появления буквы h на букву H,')
print('кроме первого и последнего вхождения.')
print()

ans = 'y'

while ans == 'y':
    s = input('строка: ')
    print(s[: s.find('h') + 1] + \
          s[s.find('h') + 1 : s.rfind('h')].replace('h', 'H') + \
          s[s.rfind('h') :])
    ans = input('Еще раз? y/n ')
