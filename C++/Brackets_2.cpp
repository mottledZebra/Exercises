// Перебор правильных скобочных последовательностей с двумя типами скобок. 
// Выведите все правильные скобочные последовательности с двумя типами скобок '(', ')', '[', ']', 
// содержащие 2n скобок, в лексикографическом порядке. 
// В последовательности могут встречаться оба типа скобок или только один из них.
//
// Входные данные
// Натуральное число n.
//
// Выходные данные
// Выведите все правильные скобочные последовательности в лексикографическом порядке, 
// каждую последовательность - в отдельной строке, без пробелов. Считайте, что '(' < ')' < '[' < ']'.
//
// Решение рекурсивным перебором

#include <iostream>
#include <fstream>
#include <stack>
#include <vector>

using namespace std;

void out(const vector<char> &s);
void sqbr(vector<char> &str, int idx, stack<char> &br);

int main()
{
    setlocale(LC_ALL, "ru");

    int n;
    cout << "Введите число пар скобок" << endl;
    cin >> n;

    vector<char> s(2 * n);
    stack<char> br;    
    sqbr(s, 0, br);

    cout << "Ответ в файле \"output.txt\"" << endl;

    system("pause");
    return 0;
}

void sqbr(vector<char> &str, int idx, stack<char> &br)
{
    if (idx == str.size())
    {
        if (!br.size())
            out(str);
        return;
    }

    str[idx] = '(';
    br.push('(');
    sqbr(str, idx + 1, br);
    br.pop();

    if (br.size() && br.top() == '(')
    {
        str[idx] = ')';
        br.pop();
        sqbr(str, idx + 1, br);
        br.push('(');
    }

    str[idx] = '[';
    br.push('[');
    sqbr(str, idx + 1, br);
    br.pop();

    if (br.size() && br.top() == '[')
    {
        str[idx] = ']';
        br.pop();
        sqbr(str, idx + 1, br);
        br.push('[');
    }
}

void out(const vector<char> &s)
{
    static int c;
    ofstream coutf;

    if (c) coutf.open("output.txt", ios_base::app);
    else coutf.open("output.txt");

    coutf << ++c << "\t";

    for (auto i : s) coutf << i << " ";

    coutf << endl;

    coutf.close();
}
