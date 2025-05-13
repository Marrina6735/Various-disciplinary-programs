#include <iostream>
#include <cmath>
#include <vector>
#include <SFML/Graphics.hpp>

struct Point {
    double x, y;
    Point(double x, double y) : x(x), y(y) {}
};

void koch_snowflake(int order, double length, double angle, double x, double y, std::vector<Point>& coordinates) {
    if (order == 0) {
        coordinates.emplace_back(x, y);
        x += length * cos(angle);
        y += length * sin(angle);
        coordinates.emplace_back(x, y);
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

void generate_koch_snowflake(int order, double length, std::vector<Point>& coordinates) {
    coordinates.clear();
    double x = 0, y = 0;
    double angle = 0;
    koch_snowflake(order, length, angle, x, y, coordinates);
    coordinates.emplace_back(coordinates.front());  // Замыкаем снежинку
}

int main() {
    // Установите значение order и length по вашему желанию
    int order = 4;
    double length = 300.0;

    std::vector<Point> snowflake_coordinates;

    // Генерируем координаты замкнутой снежинки Коха
    generate_koch_snowflake(order, length, snowflake_coordinates);

    // Выводим координаты замкнутой снежинки
    for (const auto& point : snowflake_coordinates) {
        std::cout << "(" << point.x << ", " << point.y << ")" << std::endl;
    }

    // Отображение замкнутой снежинки в окне
    sf::RenderWindow window(sf::VideoMode(600, 600), "Koch Snowflake");
    window.clear();

    sf::VertexArray lines(sf::LinesStrip);
    for (const auto& point : snowflake_coordinates) {
        lines.append(sf::Vertex(sf::Vector2f(point.x + 300, point.y + 300), sf::Color::Blue));
    }

    window.draw(lines);
    window.display();

    while (window.isOpen()) {
        sf::Event event;
        while (window.pollEvent(event)) {
            if (event.type == sf::Event::Closed) {
                window.close();
            }
        }
    }

    return 0;
}