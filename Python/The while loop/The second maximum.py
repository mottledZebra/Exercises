# Последовательность состоит из различных натуральных чисел
# и завершается числом 0. Определите значение второго
# по величине элемента в этой последовательности.
# Гарантируется, что в последовательности есть хотя бы два элемента.

# The sequence consists of distinct natural numbers
# and ends with the number 0. Determine the value of the second
# largest element in this sequence.
# It is guaranteed that the sequence has at least two elements.

print('Последовательность состоит из различных натуральных чисел')
print('и завершается числом 0. Определить значение второго')
print('по величине элемента в этой последовательности.')
print('Гарантируется, что в последовательности есть хотя бы два элемента.')
print()

ans = 'y'

while ans == 'y':
    max1 = int(input('a1 = '))
    max2 = n = int(input('a2 = '))
    i = 2
    if max2 > max1:
        max1, max2 = max2, max1
    while n != 0:
        i += 1
        n = int(input('a' + str(i) + ' = '))
        if n > max1:
            max2 = max1
            max1 = n
        elif n > max2:
            max2 = n
    print('Второй максимум = ' + str(max2))
    ans = input('Еще раз? y/n ')
