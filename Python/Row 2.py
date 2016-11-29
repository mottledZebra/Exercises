# Даны два целых числа A и В. Выведите все числа от A до B включительно,
# в порядке возрастания, если A < B, или в порядке убывания в противном случае.  

# Given two integers A and B. Output all the numbers from A to B, inclusive,
# in ascending order, if A < B, or in descending order otherwise.

print('Даны два целых числа A и В. Вывести все числа от A до B включительно,')
print('в порядке возрастания, если A < B, или в порядке убывания в противном случае.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('A = '))
    b = int(input('B = '))
    c = 1
    if a >= b:
        c = -1
    for i in range(a, b + c, c):
        print(i)
    ans = input('Еще раз? y/n ')
