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
// Решение динамикой по битовым маскам

#include <iostream>
#include <fstream>
#include <vector>
//#include <algorithm>

using namespace std;

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

    vector<vector<int>> a(n, vector<int>(n));
    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            cinf >> a[i][j];

    cinf.close();

    vector<vector<int>> p((1 << n), vector<int>(n, 0));
    vector<vector<int>> d((1 << n), vector<int>(n, INT_MAX));
    d[0][0] = 0;

    for (int mask = 0; mask < (1 << n); mask++)     // динамика
        for (int i = 0; i < n; i++)
        {
            if (d[mask][i] == INT_MAX)
                continue;
            for (int j = 0; j < n; j++)
                if (!(mask & (1 << j)))
                {
                    if (d[mask][i] + a[i][j] < d[mask ^ (1 << j)][j])
                    {
                        d[mask ^ (1 << j)][j] = d[mask][i] + a[i][j];
                        p[mask ^ (1 << j)][j] = i;
                    }
                }
        }

    cout << d[(1 << n) - 1][0] << endl;  // минимальный путь

    cout << "0";
    int mask = (1 << n) - 1;
    int i = 0;
    for (int j = 0; j < n - 1; j++)     // вывод минимального маршрута
    {
        int l = p[mask][i];
        mask = mask ^ (1 << i);
        i = l;
        cout << " " << i;
    }
    cout << endl;

    system("pause");
    return 0;
}

