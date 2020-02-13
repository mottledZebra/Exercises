// базовый абстрактный класс фигуры
#pragma once
#include <windows.h>

namespace nsShape
{
    class Point
    {
    public:
        int first;
        int second;
    };

    class Shape
    {
    public:
        Shape() :X(), Y()   // конструктор по умолчанию
        {
        }
        Shape(int x, int y) :X(x), Y(y)   // конструктор с параметрами
        {
        }
        virtual ~Shape()    // виртуальный деструктор, д.б. реализован в каждом классе-наследнике
        {
        }

        virtual void draw(HDC hdc) = 0; // чисто виртуальная функция отрисовки фигуры
                                        // должна быть реализована в каждом классе-наследнике

        void setCoord(int x, int y) // установка координат фигуры
        {
            X = x;
            Y = y;
        }

        void setCoord(Point c) // установка координат фигуры через класс Point
        {
            X = c.first;
            Y = c.second;
        }

        Point getCoord()      // получение координат фигуры
        {
            Point p;
            p.first = X;
            p.second = Y;

            return p;
        }

    protected:
        int X;   // координаты начала фигуры
        int Y;
    };
}

