// класс прямоугольника, потомок класса квадрата
#pragma once
#include "Square.h"

namespace nsShape
{
    class Rectangle :
        public Square
    {
    public:
        Rectangle() : E2()   // конструктор по умолчанию
        {
        }
        Rectangle(int e, int e2) : Square(e), E2(e2) // конструктор с заданием сторон, координаты по умолчанию
        {
        }
        Rectangle(int x, int y, int e, int e2) : Square(x, y, e), E2(e2)   // конструктор с параметрами
        {
        }
        ~Rectangle()
        {
        }

        void draw(HDC hdc)  // отрисовка; привязка координат в левом верхнем углу
        {
            for (int i = X; i <= X + E; i++)
            {
                SetPixel(hdc, i, Y, RGB(255, 255, 255));
            }
            for (int i = Y; i <= Y + E2; i++)
            {
                SetPixel(hdc, X + E, i, RGB(255, 255, 255));
            }
            for (int i = X + E; i >= X; i--)
            {
                SetPixel(hdc, i, Y + E2, RGB(255, 255, 255));
            }
            for (int i = Y + E2; i >= Y; i--)
            {
                SetPixel(hdc, X, i, RGB(255, 255, 255));
            }
        }

        void setEdges(Point e) // установка сторон прямоугольника
        {
            E = e.first;
            E2 = e.second;
        }

        Point getEdges()     // получение сторон прямоугольника
        {
            Point e;
            e.first = E;
            e.second = E2;

            return e;
        }

    protected:
        int E2;
    };
}
