import pygame
import numpy as np

# Функция для вычисления глубины пикселя относительно плоскости
def find_depth(point, plane):
    A, B, C, D = plane
    depth = -(A * point[0] + B * point[1] + D) / C
    return round(depth)

# Функция для вычисления уравнения плоскости по трем точкам
def calculate_plane_equation(v0, v1, v2):
    normal_vector = np.cross(v1 - v0, v2 - v0)
    D = -np.dot(normal_vector, v0)
    equation = np.concatenate([normal_vector, [D]])
    return equation

# Функция для получения точек пересечения сканирующей строки с ребрами многоугольника
def get_intersections(y, coord):
    intersections = []
    n = len(coord)
    for i in range(n):
        x1, y1 = coord[i][0:2]
        x2, y2 = coord[(i + 1) % n][0:2]
        if (y1 <= y < y2) or (y2 <= y < y1):
            if x1 == x2:
                intersections.append(x1)
            else:
                x_inter = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                intersections.append(x_inter)
    intersections.sort()
    return intersections

# Функция для закраски многоугольника
def draw_polygon(coordinates, color):
    plane_equation = calculate_plane_equation(np.array(coordinates[0]), np.array(coordinates[1]), np.array(coordinates[2]))
    x0, y0, z0 = coordinates[0]
    x1, y1, z1 = coordinates[1]
    x2, y2, z2 = coordinates[2]

    ymin = max(0, int(min(y0, y1, y2)))
    ymax = min(height - 1, int(max(y0, y1, y2)))

    for y in range(ymin, ymax + 1):
        intersections = get_intersections(y, coordinates)
        for i in range(0, len(intersections), 2):
            x1, x2 = int(intersections[i]), int(intersections[i + 1])

            for x in range(x1, x2 + 1):
                depth = find_depth(np.array([x, y, 0]), plane_equation)
                if depth < z_buffer[y, x]:
                    z_buffer[y, x] = depth
                    pygame.draw.rect(screen, color, (x, y, 1, 1))

# Инициализация Pygame
width = 800
height = 800
pygame.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Закраска пространственных многоугольников')

# Чтение координат многоугольников из файла
with open('lab4', 'r') as file:
    lines = file.readlines()
    n = int(lines[0])

    # Чтение координат первого многоугольника
    coord = []
    for line in lines[2:2 + n]:
        coord.append(list(map(int, line.split())))

    # Чтение координат второго многоугольника
    n2 = int(lines[10])
    coord2 = []
    for line in lines[12:12 + n2]:
        coord2.append(list(map(int, line.split())))

# Создание списков координат x и y
x_coords = [i[0] for i in coord]
y_coords = [i[1] for i in coord]

# Определение минимальных и максимальных координат
xmin = min(x_coords)
ymin = min(y_coords)
xmax = max(x_coords)
ymax = max(y_coords)

# Инициализация Z-буфера
z_buffer = np.full((height, width), np.inf, dtype=np.float32)

# Закраска многоугольников
draw_polygon(coord, (138, 43, 226))
draw_polygon(coord2, (255, 165, 0))

# Обновление экрана Pygame
pygame.display.flip()

# Ожидание завершения программы
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Завершение Pygame
pygame.quit()
