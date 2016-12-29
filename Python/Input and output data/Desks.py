# В школе решили набрать три новых математических класса.
# Так как занятия по математике у них проходят в одно и то же время,
# было решено выделить кабинет для каждого класса и купить в них новые парты.
# За каждой партой может сидеть не больше двух учеников.
# Известно количество учащихся в каждом из трёх классов.
# Сколько всего нужно закупить парт чтобы их хватило на всех учеников?
# Программа получает на вход три натуральных числа:
# количество учащихся в каждом из трех классов. 

# The school decided to recruit three new math class.
# Since the classes in mathematics they are at the same time,
# it was decided to allocate the office for each class and to buy them new desks.
# Behind each desk can sit no more than two students.
# Know the number of students in each of the three classes.
# How much to buy desks to enough for all students?
# The program receives the input of three integers:
# the number of students in each of the three classes.

print('В школе решили набрать три новых математических класса.')
print('Так как занятия по математике у них проходят в одно и то же время,')
print('было решено выделить кабинет для каждого класса и купить в них новые парты.')
print('За каждой партой может сидеть не больше двух учеников.')
print('Известно количество учащихся в каждом из трёх классов.')
print('Сколько всего нужно закупить парт чтобы их хватило на всех учеников?')
print('Программа получает на вход три натуральных числа:')
print('количество учащихся в каждом из трех классов.')
print()

ans = 'y'

while ans == 'y':
    a = int(input('Количество учеников в первом классе: '))
    b = int(input('Количество учеников во втором классе: '))
    c = int(input('Количество учеников в третьем классе: '))
    a1 = a // 2 + a % 2
    b1 = b // 2 + b % 2
    c1 = c // 2 + c % 2
    print(str('Надо купить ' + str(a1 + b1 + c1) + ' парт'))
    ans = input('Еще раз? y/n ')
