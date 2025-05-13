import time
import pygame
from numpy import *
from math import *

# Размеры окна
screen_height: int = 600
screen_width: int = 800

# Масштаб и параметры камеры
scale = 300
d = 1
RO = 800
THETA = pi / 3
FI = pi / 6

# Инициализация Pygame
pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Куб")

def clear_screen():
    # Очистка экрана
    screen.fill((255, 255, 255))

# Функции для вращения вокруг осей координат (Эти матрицы используются для вращения вершин куба в пространстве)
def rotate_oz(alpha):
    return array([[cos(alpha), sin(alpha), 0, 0], [-sin(alpha), cos(alpha), 0, 0],
                  [0, 0, 1, 0], [0, 0, 0, 1]])

def rotate_ox(alpha):
    return array([[1, 0, 0, 0], [0, cos(alpha), sin(alpha), 0],
                  [0, -sin(alpha), cos(alpha), 0], [0, 0, 0, 1]])

def rotate_oy(alpha):
    return array([[cos(alpha), 0, sin(alpha), 0], [0, 1, 0, 0],
                  [-sin(alpha), 0, cos(alpha), 0], [0, 0, 0, 1]])

# Переход из мировой в видовую систему координат
def world_to_view(ro, theta, fi):
    # Матрица для перехода из мировых координат в видовые координаты.Задает положение камеры в пространстве
    return array([[-sin(theta), -cos(fi) * cos(theta), -sin(fi) * cos(theta), 0],
                  [cos(theta), -cos(fi) * sin(theta), -sin(fi) * sin(theta), 0],
                  [0, sin(fi), -cos(fi), 0],
                  [0, 0, ro, 1]])

def draw_figure(vertices, edges):
    clear_screen()
    for i, j in edges:
        pygame.draw.line(screen, (0, 0, 0), (vertices[i][0], vertices[i][1]), (vertices[j][0], vertices[j][1]))
    pygame.display.flip()

class Cube:
    # Вершины
    vertices = array([[1, 0, 0, 1], [0, 0, 0, 1],
                      [0, 1, 0, 1], [1, 1, 0, 1],
                      [1, 0, 1, 1], [0, 0, 1, 1],
                      [0, 1, 1, 1], [1, 1, 1, 1]])
    v = vertices

    # Рёбра
    edges = array([[0, 1], [1, 2], [2, 3], [3, 0],
                   [4, 5], [5, 6], [6, 7], [7, 4],
                   [0, 4], [1, 5], [2, 6], [3, 7]])

    # Грани
    faces = [[0, 1, 2, 3, (255, 192, 203)],  # Розовый
             [4, 5, 6, 7, (255, 0, 203)],
             [0, 4, 7, 3, (255, 192, 20)],
             [0, 4, 5, 1, (230, 230, 250)],  # Светло-фиолетовый
             [1, 5, 6, 2, (255, 12, 203)],
             [2, 6, 7, 3, (230, 230, 25)]]

    center = array([0, 0, 0, 1])
    center_v = center

    def __init__(self):
        a = list()
        for i in self.vertices:
            a.append([(i[0] - 1 / 2) * scale, (i[1] - 1 / 2) * scale, (i[2] - 1 / 2) * scale, 1])
        self.vertices = array(a)
        self.perspective_projection(RO, THETA, FI, d)

    def move_cube(self, alpha=0, betha=0, gamma=0, a=0, b=0, c=0): # Вращает куб и его центр вокруг осей OZ, OX и OY.
        for i in range(len(self.vertices)):
            self.vertices[i] = dot(self.vertices[i], rotate_oz(alpha))
            self.vertices[i] = dot(self.vertices[i], rotate_ox(betha))
            self.vertices[i] = dot(self.vertices[i], rotate_oy(gamma))
            self.vertices[i] = self.vertices[i]
        self.center = dot(self.center, rotate_oz(alpha))
        self.center = dot(self.center, rotate_ox(betha))
        self.center = dot(self.center, rotate_oy(gamma))
        self.center = self.center

    # Параллельная проекция
    def parallel_projection(self):
        a = list()
        for i in self.vertices:
            a.append([i[0] + screen_width / 2, i[1] + screen_height / 2])
        return (a, self.edges)

    # Перспективная проекция (переход в экранные координаты)
    def perspective_projection(self, ro, theta, fi, d):
        b = list()
        g = list()
        for i in range(len(self.vertices)):
            a = dot(self.vertices[i], world_to_view(ro, theta, fi))
            g.append([a[0], a[1], a[2]])
            b.append([d * a[0] * ro / (2 * a[2]) + screen_width / 2, d * a[1] * ro / (2 * a[2]) + screen_height / 2])
        self.v = g
        self.center_v = dot(self.center, world_to_view(ro, theta, fi))
        return (b, self.edges)

    # Проверка, является ли грань лицевой, 1 способ (описываем лицевые грани – против часовой стрелки, нелицевые по часовой стрелке)
    def is_front_face_h(self, a, b, c):
        ch = self.v[a][0] * ((self.v[b][1] - self.v[a][1]) * (self.v[c][2] - self.v[a][2]) -
                             (self.v[b][2] - self.v[a][2]) * (self.v[c][1] - self.v[a][1])) + self.v[a][1] * (
                     (self.v[b][2] - self.v[a][2]) * (self.v[c][0] - self.v[a][0]) -
                     (self.v[b][0] - self.v[a][0]) * (self.v[c][2] - self.v[a][2])) + self.v[a][2] * (
                     (self.v[c][1] - self.v[a][1]) * (self.v[b][0] - self.v[a][0]) -
                     (self.v[c][0] - self.v[a][0]) * (self.v[b][1] - self.v[a][1]))
        if ch > 0: # Если коэффициент уравнения плоскости положительный отрисовываем
            return True
        else:
            return False

    # Проверка, является ли грань лицевой, 2 способ (отрисовка ребер)
    def is_front_face_l(self, a, b, c):
        ca = ((self.v[b][1] - self.v[a][1]) * (self.v[c][2] - self.v[a][2]) -
              (self.v[b][2] - self.v[a][2]) * (self.v[c][1] - self.v[a][1]))
        cb = ((self.v[b][2] - self.v[a][2]) * (self.v[c][0] - self.v[a][0]) -
              (self.v[b][0] - self.v[a][0]) * (self.v[c][2] - self.v[a][2]))
        cc = ((self.v[c][1] - self.v[a][1]) * (self.v[b][0] - self.v[a][0]) -
              (self.v[c][0] - self.v[a][0]) * (self.v[b][1] - self.v[a][1]))
        ch = self.v[a][0] * ca + self.v[a][1] * cb + self.v[a][2] * cc
        cl = ca * self.center_v[0] + cb * self.center_v[1] + cc * self.center_v[2] - ch
        sgn = cl / abs(cl)
        n = array([ca, cb, cc]) * sgn
        d = array([(self.v[a][0] + self.v[b][0] + self.v[c][0]) / 3,
                   (self.v[a][1] + self.v[b][1] + self.v[c][1]) / 3,
                   (self.v[a][2] + self.v[b][2] + self.v[c][2]) / 3])
        csa = dot(d, n) / linalg.norm(n) / linalg.norm(d)
        if 0 < csa < 1: # Если угол меньше 90 градусов
            return True
        else:
            return False

    def fill_faces(self):
        flat = self.perspective_projection(RO, THETA, FI, d)[0]
        show = list()
        for f in self.faces:
            if self.is_front_face_h(f[0], f[1], f[2]):
                show.append(f)
        clear_screen()
        for k in show:
            pygame.draw.polygon(screen, pygame.Color(k[4]),
                                [(flat[k[0]][0], flat[k[0]][1]),
                                 (flat[k[1]][0], flat[k[1]][1]),
                                 (flat[k[2]][0], flat[k[2]][1]),
                                 (flat[k[3]][0], flat[k[3]][1])])
        pygame.display.flip()

# Инициализация куба
cube = Cube()

# Настройка часов Pygame
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Вращение куба и камеры
    cube.move_cube(alpha=pi / 300, betha=pi / 600, gamma=pi / 600)
    THETA += pi / 150
    FI -= pi / 150

    # Заполнение граней и отображение
    cube.fill_faces()
    time.sleep(1 / 24)

    clock.tick(60)
