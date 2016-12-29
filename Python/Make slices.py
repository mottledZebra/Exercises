# Дана строка.
# Сначала выведите третий символ этой строки.
# Во второй строке выведите предпоследний символ этой строки.
# В третьей строке выведите первые пять символов этой строки.
# В четвертой строке выведите всю строку, кроме последних двух символов.
# В пятой строке выведите все символы с четными индексами
# (считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).
# В шестой строке выведите все символы с нечетными индексами,
# то есть начиная со второго символа строки.
# В седьмой строке выведите все символы в обратном порядке.
# В восьмой строке выведите все символы строки через один в обратном порядке,
# начиная с последнего.
# В девятой строке выведите длину данной строки.  

# Given a string.
# First print the third character of this string.
# In the second line print the second last character of this string.
# In the third line print the first five characters of this string.
# In the fourth line, print the entire string except the last two characters.
# In the fifth line, print all the symbols with even indices
# (assuming that indexing starts from 0, so the characters are displayed starting with the first).
# In the sixth line, print all the symbols with odd indices,
# i.e. starting from the second character of the string.
# In the seventh line, print all the characters in reverse order.
# In the eighth line, print all the characters of the string through one in reverse
# order starting with the most recent.
# In the ninth line, print the length of the given string.

print('Дана строка.')
print('Сначала вывести третий символ этой строки.')
print('Во второй строке вывести предпоследний символ этой строки.')
print('В третьей строке вывести первые пять символов этой строки.')
print('В четвертой строке вывести всю строку, кроме последних двух символов.')
print('В пятой строке вывести все символы с четными индексами')
print('(считая, что индексация начинается с 0, поэтому символы выводятся начиная с первого).')
print('В шестой строке вывести все символы с нечетными индексами,')
print('то есть начиная со второго символа строки.')
print('В седьмой строке вывести все символы в обратном порядке.')
print('В восьмой строке вывести все символы строки через один в обратном порядке,')
print('начиная с последнего.')
print('В девятой строке вывести длину данной строки.')
print()

ans = 'y'

while ans == 'y':
    s = str(input('строка: '))
    print(s[2])
    print(s[-2])
    print(s[:5])
    print(s[:-2])
    print(s[::2])
    print(s[1::2])
    print(s[::-1])
    print(s[::-2])
    print(len(s))
    ans = input('Еще раз? y/n ')
