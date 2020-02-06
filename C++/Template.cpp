// Ўаблон. «адан шаблон, состо€щий из строчных латинских букв от 'a' до 'e' и вопросительных знаков '?'. 
// Ѕудем говорить, что строка соответствует шаблону,  если она получаетс€ из шаблона 
// заменой всех вопросительных знаков на строчные латинские буквы от 'a' до 'e'. 
// ≈сли вопросительных знаков в шаблоне несколько, они могут быть заменены на разные буквы. 
// Ќапример, шаблону "a?b?" соответствуют строки "aabc", "aebd", "aaba" и др. 
// ¬ыведите все строки, соответствующие данному шаблону, в лексикографическом пор€дке.
//
// ¬ходные данные
// Ўаблон - строка, состо€ща€ из строчных латинских букв от 'a' до 'e' и вопросительных знаков '?'.
//
// ¬ыходные данные
// ¬ыведите все строки, соответствующие шаблону, в лексикографическом пор€дке.
//
// –ешение рекурсивным перебором

#include <iostream>
#include <fstream>
#include <string>
#include <vector>

using namespace std;

// вывод готовых строк в файл
void out(string& str)
{
    ofstream coutf;
    static int s;

    if (s) coutf.open("output.txt", ios_base::app);
    else   coutf.open("output.txt");

    coutf << ++s << "\t" << str[0];
    for (int i = 1; i < str.length(); i++)
        coutf << " " << str[i];
    coutf << endl;

    coutf.close();
}

// рекурсивное построение строк по шаблону
void ord(const string& temp, string& str, string& symb, int idx) 
{
    if (idx == temp.length())
    {
        out(str);
        return;
    }

    if (temp[idx] != '?')
    {
        str[idx] = temp[idx];
        ord(temp, str, symb, idx + 1);
    }
    else
        for (int i = 0; i < symb.length(); i++)
        {
            str[idx] = symb[i];
            ord(temp, str, symb, idx + 1);
        }
}

int main()
{
    setlocale(LC_ALL, "ru");

    string temp;
    cout << "¬ведите шаблон" << endl;
    cin >> temp;

    string str(temp.length(), '?');
    string symb = "abcde";

    ord(temp, str, symb, 0);

    cout << "ќтвет в файле \"output.txt\"" << endl;

    system("pause");
    return 0;
}


