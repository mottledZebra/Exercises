# Дана строка. Разрежьте ее на две равные части (если длина строки — четная,
# а если длина строки нечетная, то длина первой части должна быть на один символ больше).
# Переставьте эти две части местами, результат запишите в новую строку и выведите на экран.
# При решении этой задачи не пользоваться инструкцией if. 

# Given a string. Cut it into two equal parts (if the length of string is even,
# and if the string length is odd, then the length of the first part should be one character more).
# Move these two parts interchanged, write the result to a new string and put it on the screen.
# In solving this problem is not to use the if statement.

print('Дана строка. Разрезать ее на две равные части (если длина строки — четная,')
print('а если длина строки нечетная, то длина первой части должна быть на один символ больше).')
print('Переставить эти две части местами, результат записать в новую строку и вывести на экран.')
print('При решении этой задачи не используется инструкция if.')
print()

ans = 'y'

while ans == 'y':
    s = input('строка: ')
    s1 = s[-1 * (len(s) // 2) :]
    s2 = s[: -1 * (len(s) // 2)]
    print(s1 + s2)
    ans = input('Еще раз? y/n ')
