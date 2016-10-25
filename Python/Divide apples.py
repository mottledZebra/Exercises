# n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.
# Сколько яблок достанется каждому школьнику?
# Сколько яблок останется в корзинке?
# Программа получает на вход числа n и k и должна вывести искомое количество яблок (два числа).

# n students divide k apples equally, nonproliferating residue remains in the basket.
# How many apples will each student get?
# How many apples remain in the basket?
# The program takes on input the numbers n and k, and should output the desired number of apples (two numbers).

print('n школьников делят k яблок поровну, неделящийся остаток остается в корзинке.')
print('Сколько яблок достанется каждому школьнику?')
print('Сколько яблок останется в корзинке?')

n = int(input('n = '))
k = int(input('k = '))

print(str(k // n) + ' яблок получит каждый школьник')
print(str(k % n) + ' яблок останется в корзинке')
