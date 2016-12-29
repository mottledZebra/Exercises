# Напишите программу, которая считывает три числа и выводит их сумму. 
# Каждое число записано в отдельной строке. 

# Write a program that reads three numbers and prints their sum. 
# Each number is written in a separate line.

print('Сумма трех чисел')
print()

ans = 'y'

while ans == 'y':
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    sum = a + b + c
    print('Сумма = ' + str(sum))
    ans = input('Еще раз? y/n ')
