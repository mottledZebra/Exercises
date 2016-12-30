# Дана строка, в которой буква h встречается минимум два раза.
# Удалите из этой строки первое и последнее вхождение буквы h,
# а также все символы, находящиеся между ними. 

# Given a string where the letter h occurs at least twice.
# Remove from this line first and last occurrence of the letter h,
# and all characters that are between them.

print('Дана строка, в которой буква h встречается минимум два раза.')
print('Удалить из этой строки первое и последнее вхождение буквы h,')
print('а также все символы, находящиеся между ними.')
print()

ans = 'y'

while ans == 'y':
    s = input('строка: ')
    print(s[: s.find('h')] + s[s.rfind('h') + 1 :])
    ans = input('Еще раз? y/n ')
