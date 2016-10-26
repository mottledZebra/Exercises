# Напишите программу, которая приветствует пользователя, выводя слово Hello,
# введенное имя и знаки препинания по образцу: Hello, Harry!

# Write a program that greets the user, output the word Hello
# and the name entered punctuation marks on the model: Hello, Harry!

print('Напишите программу, которая приветствует пользователя, выводя слово Hello,')
print('введенное имя и знаки препинания по образцу: Hello, Harry!')
print()

ans = 'y'

while ans == 'y':
    s = input('Как Вас зовут? ')
    print('Hello, ' + s + '!')
    ans = input('Еще раз? y/n ')
