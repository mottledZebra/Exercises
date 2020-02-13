// класс окружности, потомок класса фигуры
#pragma once
#define _USE_MATH_DEFINES
#include "Shape.h"
#include <math.h>

namespace nsShape
{
    class Circle :
        public Shape
    {
    public:
        Circle() : R()   // конструктор по умолчанию   
        {
        }
        Circle(int r) : R(r) // конструктор с заданием радиуса, координаты по умолчанию
        {
        }
        Circle(int x, int y, int r) : Shape(x, y), R(r)   // конструктор с параметрами
        {
        }
        ~Circle()
        {
        }

        void draw(HDC hdc)  // отрисовка; привязка координат в центре окружности
        {
            for (float i = 0; i < M_PI * 2; i += 0.001)
            {
                SetPixel(hdc, X + R * cos(i), Y + R * sin(i), RGB(255, 255, 255));
            }
        }

        void setRadius(int r) // установка радиуса окружности
        {
            R = r;
        }

        int getRadius()     // получение радиуса окружности
        {
            return R;
        }

    protected:
        int R;
    };
}

