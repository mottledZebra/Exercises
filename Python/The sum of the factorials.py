# По данному натуральном n вычислите сумму 1!+2!+3!+...+n!.
# В решении этой задачи можно использовать только один цикл.
# Пользоваться математической библиотекой math в этой задаче запрещено. 

# For the given natural n calculate the sum 1!+2!+3!+...+n!.
# In this task, you can only use one cycle.
# To use the math library in this problem is prohibited.

print('По данному натуральному n вычислить сумму 1!+2!+3!+...+n!')
print()

ans = 'y'

while ans == 'y':
    n = int(input('n = '))
    s = 0
    p = 1
    for i in range(1, n + 1):
        p *= i
        s += p
    print('сумма n! = ' + str(s))
    ans = input('Еще раз? y/n ')
