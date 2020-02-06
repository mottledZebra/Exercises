// Арифметическое выражение. Даны n чисел a1, a2, …, an​. 
// Расставьте между ними плюсы '+' и минусы '-', чтобы значение полученного выражения было равно x.
//
// Входные данные
// В первой строке заданы два целых числа - n и x.
// Во второй строке содержатся целые положительные числа a1, a2, …, an​.
//
// Выходные данные
// Выведите арифметическое выражение, значение которого равно x.
// Числа в выражении должны идти в том же порядке, что и во входном файле.
// Необходимо использовать все числа.Между каждой парой чисел  должен быть знак '+' или '-'.
// Минус перед первым числом ставить нельзя.
//
// Решение динамическим программированием

#include <iostream>
#include <fstream>
#include <vector>

using namespace std;

void out(const vector<int> &c, const vector<vector<int>> &p, int i, int s)
{
    if (i <= 0) return;

    out(c, p, i - 1, s - p[i][s] * c[i]);

    if (p[i][s] == 1) 
        cout << "+";
    else if (p[i][s] == -1) 
        cout << "-";    
    cout << c[i];
}

int main()
{
    setlocale(LC_ALL, "ru");

    int n, sum;
    string fn;
    ifstream cinf;

    cout << "Введите имя файла" << endl;
    cin >> fn;
    cinf.open(fn);
    cinf >> n >> sum;

    vector<int> c(n);
    for (int i = 0; i < n; i++)
        cinf >> c[i];
    cinf.close();

    int sMin = c[0];
    int sMax = c[0];
    for (int i = 1; i < n; i++)     // определяем границы динамики - минимальный и максимальный результат выражения
    {
        sMin -= c[i];
        sMax += c[i];
    }
    int sAll = sMax - sMin + 1;

    vector<vector<int>> p(n, vector<int>(sAll, 0));
    p[0][c[0] + abs(sMin)] = 1;
    for (int i = 1; i < n; i++)             // вычисление динамики
        for (int j = 0; j < sAll; j++)
            if (p[i - 1][j])
            {
                p[i][j + c[i]] = 1;
                p[i][j - c[i]] = -1;
            }

    cout << c[0];
    out(c, p, n - 1, sum + abs(sMin));      // рекурсивный вывод выражения
    cout << endl;

    system("pause");
    return 0;
}

