# Дана строка. Если в этой строке буква f встречается только один раз,
# выведите её индекс. Если она встречается два и более раз,
# выведите индекс её первого и последнего появления.
# Если буква f в данной строке не встречается, ничего не выводите. 

# Given a string. If in this line the letter "f" occurs only once,
# then output its index. If it occurs two or more times,
# print the index of its first and last appearance.
# If the letter "f" in the string is not found, nothing to print.

print('Дана строка. Если в этой строке буква f встречается только один раз,')
print('выводится её индекс. Если она встречается два и более раз,')
print('выводится индекс её первого и последнего появления.')
print('Если буква f в данной строке не встречается, ничего не выводится.')
print()

ans = 'y'

while ans == 'y':
    s = input('строка: ')
    s1 = s.find('f')
    s2 = s.rfind('f')
    if s1 >= 0:
        if s2 == s1:
            print('Первый индекс: ' + str(s1))
        else:
            print('Первый индекс: ' + str(s1) + ', последний индекс: ' + str(s2))
    else:
        print('Буква f не встречается')
    ans = input('Еще раз? y/n ')
