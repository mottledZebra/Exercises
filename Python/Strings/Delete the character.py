# Дана строка. Удалите из этой строки все символы @. 

# Given a string. Remove from this string all the characters @.

print('Дана строка. Удалить из этой строки все символы @.')
print()

ans = 'y'

while ans == 'y':
    print(input('строка: ').replace('@', ''))
    ans = input('Еще раз? y/n ')
