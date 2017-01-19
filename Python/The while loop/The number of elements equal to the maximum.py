# Последовательность состоит из различных натуральных чисел
# и завершается числом 0. Определите, сколько элементов
# этой последовательности равны ее наибольшему элементу. 

# The sequence consists of distinct natural numbers
# and ends with the number 0. Determine how many elements
# of this sequence is equal to its largest element.

print('Последовательность состоит из различных натуральных чисел')
print('и завершается числом 0. Определить, сколько элементов')
print('этой последовательности равны ее наибольшему элементу.')
print()

ans = 'y'

while ans == 'y':
    max = n = int(input('a1 = '))
    k = i = 1
    while n != 0:
        i += 1
        n = int(input('a' + str(i) + ' = '))
        if n > max:
            max = n
            k = 1
        elif n == max:
            k += 1
    print(k)
    ans = input('Еще раз? y/n ')
