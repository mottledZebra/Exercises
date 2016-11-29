# Даны два целых числа A и B (при этом A ≤ B).
# Выведите все числа от A до B включительно. 

# Given two integers A and B (with A ≤ B).
# Print all integers from A to B, inclusive.

print('Даны два целых числа A и B (при этом A ≤ B).')
print('Вывести все числа от A до B включительно.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('A = '))
    b = int(input('B = '))
    for i in range(a, b+1):
        print(i)
    ans = input('Еще раз? y/n ')
