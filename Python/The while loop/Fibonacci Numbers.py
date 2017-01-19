# Последовательность Фибоначчи определяется так:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
# По данному числу n определите n-е число Фибоначчи φn.  

# The Fibonacci sequence is defined as
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
# On the number n, define the n-th Fibonacci number.

print('Последовательность Фибоначчи определяется так:')
print('φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.')
print('По данному числу n определить n-е число Фибоначчи φn.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('n = '))
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        f2 = 0
        f1 = 1
        for i in range(2, n + 1):
            f = f1 + f2
            f2, f1 = f1, f
        print(f)
    ans = input('Еще раз? y/n ')
