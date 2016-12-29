# По данному натуральном N вычислите сумму 1^3+2^3+3^3+...+N^3.

# At given natural N calculate the sum 1^3+2^3+3^3+...+N^3.

print('По данному натуральном N вычислить сумму 1^3+2^3+3^3+...+N^3.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    s = 0
    for i in range(1, n + 1):
        s += (i ** 3)
    print(s)
    ans = input('Еще раз? y/n ')
