# Дана строка, в которой буква h встречается минимум два раза.
# Разверните последовательность символов, заключенную между первым
# и последним появлением буквы h, в противоположном порядке.  

# Given a string where the letter h occurs at least twice.
# Turn a sequence of characters enclosed between the first
# and last appearance of the letter h, in the opposite order.

print('Дана строка, в которой буква h встречается минимум два раза.')
print('Развернуть последовательность символов, заключенную между первым')
print('и последним появлением буквы h, в противоположном порядке.')
print()

ans = 'y'

while ans == 'y':
    s = input('строка: ')
    print(s[: s.find('h') + 1] + \
          s[s.rfind('h') - 1 : s.find('h') : -1] +\
          s[s.rfind('h') :])
    ans = input('Еще раз? y/n ')
