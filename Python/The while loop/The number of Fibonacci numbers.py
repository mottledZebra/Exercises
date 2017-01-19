# Дано натуральное число A. Определите, каким по счету числом Фибоначчи
# оно является, то есть выведите такое число n, что φn = A.
# Если А не является числом Фибоначчи, выведите число -1.  

# Given a positive integer A. Determine which Fibonacci number
# it is, i.e. output a number n that φn = A.
# If A is not a Fibonacci number, print number -1.

print('Дано натуральное число A. Определить, каким по счету числом Фибоначчи')
print('оно является, то есть вывести такое число n, что φn = A.')
print('Если А не является числом Фибоначчи, вывести число -1.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('A = '))
    if a == 0:
        print(0)
    else:
        n1 = 0
        n2 = 1
        i = 1
        while n2 < a:
            n1, n2 = n2, n1 + n2
            i += 1
        if n2 == a:
            print(i)
        else:
            print(-1)
    ans = input('Еще раз? y/n ')
