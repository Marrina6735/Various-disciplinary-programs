import numpy as np
import pygame
from math import pi, cos, sin

height = 500 # Размер экрана
width = 500
scale = 300  # Масштаб

pygame.init()
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Поворот каркасного куба")

def clear_screen(): # Чистка экрана
    pygame.display.flip()
    pygame.time.delay(16)  # Задержка для контроля частоты кадров
    window.fill((255, 255, 255))

def rotate_around_z(alpha): # Поворот относительно оси OZ
    return np.array([[cos(alpha), sin(alpha), 0, 0],
                     [-sin(alpha), cos(alpha), 0, 0],
                     [0, 0, 1, 0],
                     [0, 0, 0, 1]])

def rotate_around_x(alpha): # Поворот относительно оси OX
    return np.array([[1, 0, 0, 0],
                     [0, cos(alpha), sin(alpha), 0],
                     [0, -sin(alpha), cos(alpha), 0],
                     [0, 0, 0, 1]])

def rotate_around_y(alpha): # Поворот относительно оси OY
    return np.array([[cos(alpha), 0, sin(alpha), 0],
                     [0, 1, 0, 0],
                     [-sin(alpha), 0, cos(alpha), 0],
                     [0, 0, 0, 1]])

ro = 600 # Расстояние от точки наблюдения до центра проекции
theta = pi / 6 # Угол поворота вокруг оси Z. Направление взгляда наблюдателя
phi = pi / 3 # Угол поворота вокруг оси Y. Наклон наблюдателя вверх и вниз.

def view_transformation(ro, theta, phi): # Функция для перехода из мировой в видовую систему координат (мировые связаны с центром объекта наблюдения)
    return np.array([[-sin(theta), -cos(phi) * cos(theta), -sin(phi) * cos(theta), 0],
                     [cos(theta), -cos(phi) * sin(theta), -sin(phi) * sin(theta), 0],
                     [0, sin(phi), -cos(phi), 0],
                     [0, 0, ro, 1]])

def draw_cube(vertices, edges): # Создание куба по вершинам и ребрам
    clear_screen()
    for i, j in edges:
        pygame.draw.line(window, (0, 0, 255), (vertices[i][0], vertices[i][1]), (vertices[j][0], vertices[j][1]))
    pygame.display.flip()

class Cube:
    vertices = np.array([[1, 0, 0, 1], # Вершины каркасного куба
                         [0, 0, 0, 1],
                         [0, 1, 0, 1],
                         [1, 1, 0, 1],
                         [1, 0, 1, 1],
                         [0, 0, 1, 1],
                         [0, 1, 1, 1],
                         [1, 1, 1, 1]])

    edges = np.array([[0, 1], # Ребра каркасного куба
                      [1, 2],
                      [2, 3],
                      [3, 0],
                      [4, 5],
                      [5, 6],
                      [6, 7],
                      [7, 4],
                      [0, 4],
                      [1, 5],
                      [2, 6],
                      [3, 7]])

    center = np.array([0, 0, 0, 1])

    def __init__(self):
        a = list()
        for i in self.vertices:
            a.append([(i[0] - 1 / 2) * scale, (i[1] - 1 / 2) * scale, (i[2] - 1 / 2) * scale, 1])  # Пересчет значений с учетом масштаба
        self.vertices = np.array(a)
        self.apply_perspective(ro, theta, phi)

    def rotate_cube(self, alpha, beta, gamma): # Поворот куба
        for i in range(len(self.vertices)):
            self.vertices[i] = np.dot(self.vertices[i], rotate_around_z(alpha))  # Умножение матрицы на вектор
            self.vertices[i] = np.dot(self.vertices[i], rotate_around_x(beta))
            self.vertices[i] = np.dot(self.vertices[i], rotate_around_y(gamma))

    # Параллельная проекция
    def parallel_projection(self):
        a = list()
        for i in self.vertices:
            a.append([i[0] + width / 2, i[1] + height / 2])
            # Смещение на половину ширины и высоты экрана, чтобы оказаться в его центре
        return a, self.edges

    # Перспективная проекция
    def apply_perspective(self, ro, theta, phi):
        b = list()  # Создание массива
        for i in range(len(self.vertices)):  # Пробег по всем вершинам
            a = np.dot(self.vertices[i], view_transformation(ro, theta, phi))  # Задается положение и ориентация камеры. Применяется переход от мировых к видовым координатам
            b.append([a[0] * ro / (2 * a[2]) + width / 2, a[1] * ro / (2 * a[2]) + height / 2])  # Уменьшает размер объектов, находящихся дальше от камеры. В конце координаты смещаются, чтобы объект оказался в центре экрана. Переход из трехмерной системы в двумерную
        return b, self.edges

cube = Cube()  # Задаем куб

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    cube.rotate_cube(alpha=-pi / 300, beta=-pi / 600, gamma=-pi / 600)
    a = cube.apply_perspective(ro, theta, phi)
    draw_cube(a[0], a[1])

pygame.quit()
