// Реализуйте функцию getline, которая считывает поток ввода посимвольно, 
// пока не достигнет конца потока или не встретит символ переноса строки ('\n'), 
// и возвращает C-style строку с прочитанными символами.
// Обратите внимание, что так как размер ввода заранее неизвестен, 
// то вам нужно будет перевыделять память в процессе чтения, 
// если в потоке ввода оказалось больше символов, чем вы ожидали.
// Память, возвращенная из функции будет освобождена оператором delete[]. 
// Символ переноса строки ('\n') добавлять в строку не нужно, но не забудьте, 
// что в конце C-style строки должен быть завершающий нулевой символ


#include <iostream>
using namespace std;

char *resize(const char *str, unsigned size, unsigned new_size)
{
    char *m = new char[new_size];
    int re_size = size < new_size ? size : new_size;
    
    for (int i = 0; i < re_size; i++)
    {
        m[i] = str[i];
    }  
    delete [] str;
    
    return m;
}

char *getline()
{
    int i = 0;
    int size = 1000;
    char *str = new char[size];
    
    while (cin.get(str[i]))
    {
        if (str[i] == '\n')
            break;
        if (++i >= size)
        {
            str = resize(str, size, size += 10);
        }
    }
    str[i] = '\0';
    
    return str;
}
