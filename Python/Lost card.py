# Для настольной игры используются карточки с номерами от 1 до N.
# Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.
# Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).
# Программа должна вывести номер потерянной карточки.
# Массивами и аналогичными структурами данных пользоваться нельзя. 

# For the Board game uses cards with numbers from 1 to N.
# One card was lost. Find her, knowing the numbers for the remaining cards.
# Given a number N, then N − 1 number of remaining cards (different numbers from 1 to N).
# The program should output the number of lost cards.
# Arrays and similar data structures can not be used.

print('Для настольной игры используются карточки с номерами от 1 до N.')
print('Одна карточка потерялась. Найдите ее, зная номера оставшихся карточек.')
print('Дано число N, далее N − 1 номер оставшихся карточек (различные числа от 1 до N).')
print('Программа выводит номер потерянной карточки.')
print('Задача решена без использования массивов и аналогичных структур')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    s = n * (n + 1) / 2
    for i in range(0, n - 1):
        s -= int(input('a' + str(i + 1) + ' = '))
    print(s)
    ans = input('Еще раз? y/n ')
