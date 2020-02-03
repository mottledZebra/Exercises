// Расстановка фишек. Имеется полоса размера 1×n, разбитая на единичные клетки. 
// Нужно расставить в клетках полосы m фишек, чтобы никакие две фишки 
// не стояли в соседних клетках. Выведите все возможные расстановки.
//
// Входные данные
// Натуральные числа n и m.
//
// Выходные данные
// Выведите все корректные расстановки фишек.
// Каждая расстановка должна быть выведена в отдельной строке.
// Клетки, занятые фишками, обозначаются символами '*', свободные клетки - точками '.'. 
// Выводите расстановки в лексикографическом порядке, считая, что '*' < '.'.
//
// Решение рекурсивным перебором

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void out(const vector<char> &s);
void chip(vector<char> &s, int idx, int count, int m);

int main()
{
    setlocale(LC_ALL, "ru");

    int n, m;    
    cout << "Введите n, m" << endl;
    cin >> n >> m;

    vector<char> s(n, '.');
    chip(s, 0, 0, m);

    cout << "Ответ в файле \"output.txt\"" << endl;
    
    system("pause");
    return 0;
}

void chip(vector<char> &s, int idx, int count, int m)
{
    if (count == m)
    {
        out(s);
        return;
    }

    for (int i = idx; i < s.size(); i++)
    {
        if (i) 
            s[i - 1] = '.';
        s[i] = '*';
        chip(s, i + 2, count + 1, m);
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

