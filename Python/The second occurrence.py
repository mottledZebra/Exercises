# Дана строка. Найдите в этой строке второе вхождение буквы f,
# и выведите индекс этого вхождения. Если буква f в данной строке
# встречается только один раз, выведите число -1,
# а если не встречается ни разу, выведите число -2.  

# Given a string. Find in this string, the second occurrence of the letter f,
# and output the index of this entry. If the letter f in this string
# occurs only once, print the number -1,
# and if not found never, output the number -2.

print('Дана строка. Найдите в этой строке второе вхождение буквы f,')
print('и выведите индекс этого вхождения. Если буква f в данной строке')
print('встречается только один раз, выведите число -1,')
print('а если не встречается ни разу, выведите число -2.')
print()

ans = 'y'

while ans == 'y':
    s = input('строка: ')
    if s.count('f') >= 2:
        print('второй индекс: ' + str(s.find('f', s.find('f') + 1)))
    elif s.count('f') == 1:
        print('-1')
    else:
        print(-2)
    ans = input('Еще раз? y/n ')
