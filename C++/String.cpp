// простой аналог стандартного класса string для работы со строками

#include <cstddef> // size_t
#include <cstring> // strlen, strcpy

struct String {

	// конструктор 
	String(const char *str = "")
    {
        size = strlen(str);
        this->str = new char[size + 1];
        strcpy(this->str, str);
    }

	// заполняющий конструктор
	String(size_t n, char c)
    {
        size = n;
        str = new char[size + 1];
        for (int i = 0; i < size; i++)
        {
            str[i] = c;
        }
        str[size] = '\0';
    }

	// конструктор копирования
	String(const String &other)
    {
        size = other.size;
        str = new char[size + 1];
        for (int i = 0; i < size; i++)
        {
            str[i] = other.str[i];
        }
        str[size] = '\0';
    }

	// деструктор
	~String() 
    {
        delete [] str;
    }

	// оператор присваивания
	String &operator=(const String &other)
    {
        if (this != &other) 
        {
            delete [] str;
            size = other.size;
            str = new char[size + 1];
        
            for (int i = 0; i <= size; i++)
                str[i] = other.str[i];
        }
        
        return *this;
    }

    // оператор индекса, позволяющий задавать подстроку str[i][j], 
	// начинающуюся в позиции i (считая с 0) и заканчивающуюся в позиции j (не включая)
	const String operator[](size_t i) const
    {
        int tmp;
        String new_str("");
        
        if (beg == -1)
        {
            new_str.size = size  - i;
            new_str.beg = i;
            tmp = i;
        }
        else
        {
            new_str.size = i - beg;
            new_str.beg = -1;
            tmp = 0;
        }
        
        if (new_str.size)
        {
            String tmp_str(new_str.size, ' ');
            for (int j = 0; j < new_str.size; ++j)
            {
                tmp_str.str[j] = this->str[tmp + j];
            }
            new_str = tmp_str;
        }
        
        return new_str;
    }

	// добавление копии строки-аргумента в конец текущей строки 
	// (т.е. в конец строки, у которой он был вызван)
	void append(String &other)
    {
        size += other.size;
        char *new_str = new char[size + 1];
        
        strcpy(new_str, str);
        strcat(new_str, other.str);
        
        delete [] str;
        str = new_str;        
    }

	size_t size;	// размер строки без завершающего 0 символа
	char *str;		// указатель на C-style строку с завершающим нулевым символом
	int beg = -1;   // индекс начала подстроки
};
