# Дана строка, состоящая ровно из двух слов, разделенных пробелом.
# Переставьте эти слова местами. Результат запишите в строку
# и выведите получившуюся строку.
# При решении этой задачи не пользоваться инструкцией if. 

# Given a string consisting of exactly two words separated by a space.
# Rearrange these words in some places. Write the result to a string
# and print the resulting string.
# In solving this problem is not to use the if statement.

print('Дана строка, состоящая ровно из двух слов, разделенных пробелом.')
print('Переставить эти слова местами. Результат записать в строку')
print('и вывести получившуюся строку.')
print('При решении этой задачи не используется инструкция if.')
print()

ans = 'y'

while ans == 'y':
    s = input('строка: ')
    print(s[s.find(' ') :], s[: s.find(' ')])
    ans = input('Еще раз? y/n ')
