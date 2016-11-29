# Даны два целых числа A и В, A>B.
# Выведите все нечётные числа от A до B включительно, в порядке убывания.
# В этой задаче можно обойтись без инструкции if. 

# Given two integers A and b, A>B.
# Output all the odd numbers from A to B, inclusive, in descending order.
# In this task, you can do without an if statement.

print('Даны два целых числа A и В, A>B.')
print('Вывести все нечётные числа от A до B включительно, в порядке убывания.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('A = '))
    b = int(input('B = '))
    for i in range(((a - 1)// 2) * 2 + 1, b - 1, -2):
        print(i)
    ans = input('Еще раз? y/n ')
