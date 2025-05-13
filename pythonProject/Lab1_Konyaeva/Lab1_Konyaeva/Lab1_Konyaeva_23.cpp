#include <iostream>
#include <cmath>
#include <vector>

using namespace std;

struct Point {
    double x, y;
    Point(double x, double y) : x(x), y(y) {}
};

void koch_snowflake(int order, double length, double angle, double x, double y, vector<Point>& coordinates) {
    if (order == 0) {
        coordinates.push_back(Point(x, y));
        x += length * cos(angle);
        y += length * sin(angle);
        coordinates.push_back(Point(x, y));
    }
    else {
        length /= 3.0;
        koch_snowflake(order - 1, length, angle, x, y, coordinates);
        x += length * cos(angle);
        y += length * sin(angle);
        koch_snowflake(order - 1, length, angle - M_PI / 3.0, x, y, coordinates);
        x += length * cos(angle - M_PI / 3.0);
        y += length * sin(angle - M_PI / 3.0);
        koch_snowflake(order - 1, length, angle + M_PI / 3.0, x, y, coordinates);
        x += length * cos(angle + M_PI / 3.0);
        y += length * sin(angle + M_PI / 3.0);
        koch_snowflake(order - 1, length, angle, x, y, coordinates);
    }
}

void generate_koch_snowflake(int order, double length, vector<Point>& coordinates) {
    coordinates.clear();
    double x = 0, y = 0;
    double angle = 0;
    koch_snowflake(order, length, angle, x, y, coordinates);
}

int main() {
    // Установите значение order и length по вашему желанию
    int order = 4;
    double length = 100.0;

    vector<Point> snowflake_coordinates;

    // Генерируем координаты снежинки Коха
    generate_koch_snowflake(order, length, snowflake_coordinates);

    // Выводим координаты снежинки
    for (const auto& point : snowflake_coordinates) {
        cout << "(" << point.x << ", " << point.y << ")" << endl;
    }

    return 0;
}