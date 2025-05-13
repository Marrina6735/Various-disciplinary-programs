import pygame

# Функция для закраски многоугольника
def draw_polygon(screen, vertices, color):
    # Получаем количество вершин многоугольника
    n = len(vertices)

    # Находим минимальное и максимальное значение y среди вершин для определения границ отрисовки
    ymin = min(vertices, key=lambda vertex: vertex[1])[1]
    ymax = max(vertices, key=lambda vertex: vertex[1])[1]

    # Цикл по всем строкам, в которых может быть нарисован многоугольник
    for y in range(ymin, ymax + 1):
        intersections = []  # Список для хранения точек пересечения с ребрами

        # Цикл по всем ребрам многоугольника
        for i in range(n):
            x1, y1 = vertices[i]
            x2, y2 = vertices[(i + 1) % n]

            # Проверяем, пересекается ли текущее ребро с текущей строкой
            if y1 <= y < y2 or y2 <= y < y1:
                if y1 != y2:
                    # Вычисляем x-координату точки пересечения
                    x_inter = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    intersections.append(x_inter)

        # Сортируем точки пересечения по x
        intersections.sort()

        # Рисуем линии между парами точек пересечения для закрашивания текущей строки
        for i in range(0, len(intersections), 2):
            x1, x2 = int(intersections[i]), int(intersections[i + 1])
            pygame.draw.line(screen, color, (x1, y), (x2, y))

def main():
    pygame.init()
    width, height = 800, 800  # Задаем размеры окна
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Закраска многоугольников')

    # Задаем координаты вершин первого многоугольника
    vertices1 = [(50, 150), (600, 150), (350, 500)]
    # Задаем координаты вершин второго многоугольника
    vertices2 = [(200, 200), (500, 200), (200, 600)]

    # Вызываем функцию для закраски каждого многоугольника
    draw_polygon(screen, vertices1, (138, 43, 226))
    draw_polygon(screen, vertices2, (255, 165, 0))

    pygame.display.flip()  # Обновляем экран Pygame

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.quit()

if __name__ == "__main__":
    main()
