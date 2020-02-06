// Паркет. Имеется прямоугольное поле размера n×m. 
// Нужно посчитать число способов замостить его доминошками размера 1×2. 
// Доминошки могут быть повернуты горизонтально или вертикально, 
// но они не должны перекрываться или выходить за пределы поля. 
// Поскольку ответ может быть достаточно большим, 
// требуется вывести его по модулю k (остаток от деления ответа на k).
//
// Входные данные
// Два натуральных числа n и m - размеры поля.
//
// Выходные данные
// Одно целое число - количество способов замостить свободные клетки поля доминошками.
//
// Решение динамикой по битовым маскам

#include <iostream>
#include <vector>

using namespace std;

void comb(int a, int i, int n, vector<int>& c)  // формирование массива масок
{
    for (int j = i; j < n - 1; j++)
    {
        int b = ((1 << n) - 1) & ~(3 << j);
        c.push_back(a & b);

        comb(a & b, j + 2, n, c);
    }
}

bool can(int mask, int newMask, const vector<int> &c) // возможность перехода от старой маски к новой
{
    if (!(mask & newMask))
    {
        mask |= newMask;
        for (int i = 0; i < c.size(); i++)
            if (c[i] == mask)
                return true;
    }
    return false;
}

int main()
{
    setlocale(LC_ALL, "ru");

    int n, m, k;
    cout << "Введите размеры поля n, m и коэффициент деления k" << endl;
    cin >> n >> m >> k;

    if (n > m)
    {
        int tmp = n;
        n = m;
        m = tmp;
    }

    vector<int> c;
    c.push_back((1 << n) - 1);

    comb((1 << n) - 1, 0, n, c);

    vector<vector<long long>> d(m + 1, vector<long long>(1 << n, 0));
    d[0][0] = 1;

    for (int i = 0; i < m; i++)         // динамика
        for (int mask = 0; mask < (1 << n); mask++)
            for (int newMask = 0; newMask < (1 << n); newMask++)
                if (can(mask, newMask, c))
                {
                    d[i + 1][newMask] += d[i][mask];
                    d[i + 1][newMask] %= k;
                }
    
    cout << d[m][0] << endl;

    system("pause");
    return 0;
}

