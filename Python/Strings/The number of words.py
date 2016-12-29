# Дана строка, состоящая из слов, разделенных пробелами. Определите, сколько в ней слов.  

# Given a string consisting of words separated by spaces. Determine how many words.

print('Дана строка, состоящая из слов, разделенных пробелами. Определить, сколько в ней слов.')
print()

ans = 'y'

while ans == 'y':
    print(input('строка: ').count(' ') + 1)
    ans = input('Еще раз? y/n ')
