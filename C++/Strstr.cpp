// Напишите функцию поиска первого вхождения шаблона в текст. 
// В качестве первого параметра функция принимает текст (C-style строка), 
// в которой нужно искать шаблон. В качестве второго параметра строку-шаблон 
// (C-style строка), которую нужно найти. Функция возвращает позицию первого 
// вхождения строки-шаблона, если он присутствует в строке 
// (помните, что в C++ принято считать с 0), и -1, если шаблона в тексте нет.
// Учтите, что пустой шаблон (строка длины 0) можно найти в любом месте текста. 

int strstr(const char *text, const char *pattern)
{
    int i(0), l;

    if (!(*pattern))
        return 0;
    
    if (!(*text))
        return -1;
    
    while (*text)
    {
        l = 0;
        while (*(text + l) == *(pattern + l)) 
            l++;
        if (!(*(pattern + l)))
            return i;
        i++;
        text++;
    } 
    
    return -1;
}