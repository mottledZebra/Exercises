#include <iostream>
#include "Circle.h"
#include "Ellipse.h"
#include "Rectangle.h"
#include "Square.h"
#include "Triangle.h"

using namespace nsShape;

int main()
{
    HWND hwnd = GetConsoleWindow();
    HDC hdc = GetDC(hwnd);

    Triangle triangle(150, 150, 200);
    triangle.draw(hdc);

    Circle circle(150, 150 + 200 * sqrt(3.0) / 3, 200 * sqrt(3.0) / 3);
    circle.draw(hdc);

    nsShape::Ellipse ellipse(450, 250, 100, 200);
    ellipse.draw(hdc);

    Square square(400, 200, 100);
    square.draw(hdc);

    nsShape::Rectangle rectangle(50, 400, 300, 100);
    rectangle.draw(hdc);

    int count = 12;
    Circle* c = new Circle[count];
    for (int i = 0; i < count; i++)
    {
        (c + i)->setCoord(750 + 100 * sin(i * M_PI / 6), 300 + 100 * cos(i * M_PI / 6));
        (c + i)->setRadius(50);
        (c + i)->draw(hdc);
    }
    delete[] c;

    ReleaseDC(hwnd, hdc);
    std::cin.ignore();
    return 0;
}