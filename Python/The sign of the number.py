# В математике функция sign(x) (знак числа) определена так:
# sign(x) =  1, если x > 0,
# sign(x) = -1, если x < 0,
# sign(x) =  0, если x = 0.
# Для данного числа x выведите значение sign(x).
# Эту задачу желательно решить с использованием
# каскадных инструкций if... elif... else. 

# In mathematics the sign function(x) (number sign) are defined as follows:
# sign(x) =  1 if x > 0,
# sign(x) = -1 if x < 0,
# sign(x) =  0 if x = 0.
# For a given number x, output the value sign(x).
# This task should be solved using
# cascading instructions if ... elif ... else.

print('В математике функция sign(x) (знак числа) определена так:')
print('sign(x) =  1, если x > 0,')
print('sign(x) = -1, если x < 0,')
print('sign(x) =  0, если x = 0.')
print('Для данного числа x вывести значение sign(x).')
print()

ans = 'y'

while ans == 'y':
    x = int(input('x = '))
    print('sign(x) =', end = ' ')
    if x > 0:
        print(1)
    elif x < 0:
        print(-1)
    else:
        print(0)
    ans = input('Еще раз? y/n ')
