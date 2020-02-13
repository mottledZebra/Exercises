// класс квадрата, потомок класса фигуры
#pragma once
#include "Shape.h"

namespace nsShape
{
    class Square :
        public Shape
    {
    public:
        Square() :E()   // конструктор по умолчанию
        {
        }
        Square(int e) :E(e) // конструктор с заданием стороны, координаты по умолчанию
        {
        }
        Square(int x, int y, int e) :Shape(x, y), E(e)   // конструктор с параметрами
        {
        }
        ~Square()
        {
        }

        void draw(HDC hdc)  // отрисовка; привязка координат в левом верхнем углу
        {
            for (int i = X; i <= X + E; i++)
            {
                SetPixel(hdc, i, Y, RGB(255, 255, 255));
            }
            for (int i = Y; i <= Y + E; i++)
            {
                SetPixel(hdc, X + E, i, RGB(255, 255, 255));
            }
            for (int i = X + E; i >= X; i--)
            {
                SetPixel(hdc, i, Y + E, RGB(255, 255, 255));
            }
            for (int i = Y + E; i >= Y; i--)
            {
                SetPixel(hdc, X, i, RGB(255, 255, 255));
            }
        }

        void setEdge(int e) // установка стороны квадрата
        {
            E = e;
        }

        int getEdge()     // получение стороны квадрата
        {
            return E;
        }

    protected:
        int E;
    };
}


