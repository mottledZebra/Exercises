// Задача коммивояжера. Коммивояжер хочет объехать n городов и вернуться в исходный город. 
// Каждые два города соединены между собой дорогами, для которых известны длины. 
// Найдите путь коммивояжера минимальной длины.
//
// Входные данные
// В первой строке задано натуральное число n - количество городов.
// Следующие n строк содержат длины дорог a[i][j]​, по n чисел в каждой строке.
// Города пронумерованы числами от 0 до n−1. Гарантируется, что числа a[i][j]​ - натуральные, 
// a[i][j] = a[j][i]​ и a[i][i] = 0 для i и j от 0 до n−1.
//
// Выходные данные
// В первой строке выведите одно целое число - минимальную длину пути коммивояжера.
// Во второй строке выведите последовательность из nnn чисел - сам путь.
// Путь должен содержать номера городов в порядке обхода и начинаться с номера 0. 
//
// Решение рекурсивным перебором


#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void salesman(const vector<vector<int>>& sm, vector<int>& ans, int& alen, int idx, int len, int n)
{
    static vector<int> a(n, 0);
    static vector<bool> b(n, false);

    if (len >= alen)
        return;
    if (idx == n)
    {
        if (len + sm[a[idx - 1]][0] < alen)
        {
            alen = len + sm[a[idx - 1]][0];
            ans = a;
        }
        return;
    }
    for (int i = 1; i < n; i++)
    {
        if (b[i])
            continue;
        a[idx] = i;
        b[i] = true;
        salesman(sm, ans, alen, idx + 1, len + sm[a[idx - 1]][i], n);
        b[i] = false;
    }
}

int main()
{
    setlocale(LC_ALL, "ru");

    int n;
    string fn;
    ifstream cinf;

    cout << "Введите имя файла" << endl;
    cin >> fn;
    cinf.open(fn);
    cinf >> n;

    vector<vector<int>> sm(n, vector<int>(n, 0));
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cinf >> sm[i][j];
        }
    }
    cinf.close();

    int alen(INT_MAX);
    vector<int> ans(n, 0);

    salesman(sm, ans, alen, 1, 0, n);

    cout << alen << endl;
    for (int i = 0; i < n; i++)
    {
        cout << ans[i] << ' ';
    }
    cout << endl;
    
    system("pause");
}

