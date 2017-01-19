# Дана последовательность натуральных чисел, завершающаяся числом 0.
# Определите, какое наибольшее число подряд идущих элементов
# этой последовательности равны друг другу.  

# Given a sequence of natural numbers ending with the number 0.
# Determine what is the largest number of consecutive elements
# of this sequence are equal to each other.

print('Дана последовательность натуральных чисел, завершающаяся числом 0.')
print('Определите, какое наибольшее число подряд идущих элементов')
print('этой последовательности равны друг другу.')
print()

ans = 'y'

while ans == 'y':
    max = i = 1
    a = int(input('a1 = '))
    j = 1
    while a != 0:
        j += 1
        b = int(input('a' + str(j) + ' = '))
        if a == b:
            i += 1
        else:
            i = 1
        if max < i:
            max = i
        a = b
    print(max)
    ans = input('Еще раз? y/n ')
