// класс эллипса, потомок класса окружности
#pragma once
#include "Circle.h"

namespace nsShape
{
    class Ellipse :
        public Circle
    {
    public:
        Ellipse() : R2()   // конструктор по умолчанию
        {
        }
        Ellipse(int r, int r2) : Circle(r), R2(r2) // конструктор с заданием полуосей, координаты по умолчанию
        {
        }
        Ellipse(int x, int y, int r, int r2) : Circle(x, y, r), R2(r2)   // конструктор с параметрами
        {
        }
        ~Ellipse()
        {
        }

        void draw(HDC hdc)  // отрисовка; привязка координат в геометрическом центре 
        {
            for (float i = 0; i < M_PI * 2; i += 0.001)
            {
                SetPixel(hdc, X + R * cos(i), Y + R2 * sin(i), RGB(255, 255, 255));
            }
        }

        void setAxises(Point a) // установка полуосей эллипса
        {
            R = a.first;
            R2 = a.second;
        }

        Point getAxises()     // получение полуосей эллипса
        {
            Point a;
            a.first = R;
            a.second = R2;

            return a;
        }

    protected:
        int R2;
    };
}
