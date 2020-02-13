// класс равностороннего треугольника, потомок класса фигуры
#pragma once
#include "Shape.h"
#include <math.h>

namespace nsShape
{
    class Triangle :
        public Shape
    {
    public:
        Triangle() : E()   // конструктор по умолчанию
        {
        }
        Triangle(int e) : E(e) // конструктор с заданием стороны, координаты по умолчанию
        {
        }
        Triangle(int x, int y, int e) : Shape(x, y), E(e)   // конструктор с параметрами
        {
        }
        ~Triangle()
        {
        }

        void draw(HDC hdc)  // отрисовка; привязка координат в верхнем углу 
        {
            for (float i = X; i <= X + 0.5 * E; i += 0.1)
            {
                SetPixel(hdc, i, Y + (i - X) * float(sqrt(3.0)), RGB(255, 255, 255));
            }
            for (int i = X + 0.5 * E; i >= X - 0.5 * E; i--)
            {
                SetPixel(hdc, i, Y + E * sqrt(3.0) / 2, RGB(255, 255, 255));
            }
            for (float i = X - 0.5 * E; i <= X; i += 0.1)
            {
                SetPixel(hdc, i, Y - (i - X) * float(sqrt(3.0)), RGB(255, 255, 255));
            }
        }

        void setEdge(int e) // установка стороны треугольника
        {
            E = e;
        }

        int getEdge()     // получение стороны треугольника
        {
            return E;
        }

    protected:
        int E;
    };
}
