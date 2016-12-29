# Шоколадка имеет вид прямоугольника, разделенного на N×M долек.
# Шоколадку можно один раз разломить по прямой на две части.
# Определите, можно ли таким образом отломить от шоколадки часть,
# состоящую ровно из K долек.
# Программа получает на вход три числа: n, m, k и должна вывести YES или NO.   

# Chocolate has the form of a rectangle divided into N×M pieces.
# Chocolate can be break only once in a straight line into two parts.
# Determine whether it is possible so to break off from the chocolate part,
# consisting of exactly k pieces.
# The program receives the input of three integers: n, m, k and should display YES or NO.

print('Шоколадка имеет вид прямоугольника, разделенного на N×M долек.')
print('Шоколадку можно один раз разломить по прямой на две части.')
print('Определить, можно ли таким образом отломить от шоколадки часть,')
print('состоящую ровно из K долек.')
print('Программа получает на вход три числа: N, M, K и должна вывести YES или NO.')
print()

ans = 'y'

while ans == 'y':
    n = int(input('N = '))
    m = int(input('M = '))
    k = int(input('K = '))
    if k <= n * m and (k % m == 0 or k % n == 0):
        print('YES')
    else:
        print("NO")
    ans = input('Еще раз? y/n ')
