import pygame
import math
import numpy as np

PI = 3.1415926536

class Point:
    def __init__(self, x=0, y=0, z=0):
        self.vector = [x, y, z, 1]
        self.evector = [0, 0, 0, 0]
        self.draw = False
        self.ii = 0
        self.jj = 0

    def set_view_coord(self, theta, phi, ro):
        st = math.sin(theta)
        ct = math.cos(theta)
        sf = math.sin(phi)
        cf = math.cos(phi)
        self.draw = False
        self.evector[0] = -st * self.vector[0] + ct * self.vector[1]
        self.evector[1] = -cf * ct * self.vector[0] - cf * st * self.vector[1] + sf * self.vector[2]
        self.evector[2] = -sf * ct * self.vector[0] - sf * st * self.vector[1] - cf * self.vector[2] + ro

    def set_screen_coords(self, ro):
        x = ro * self.evector[0] / (2 * self.evector[2])
        y = ro * self.evector[1] / (2 * self.evector[2])
        xr, xl, yd, yu = 600, -300, -300, 600
        ir, il, jd, ju = 700, 0, 700, 0
        self.ii = il + ((x - xr) * (ir - il) / (xl - xr))
        self.jj = ju + ((y - yu) * (jd - ju) / (yd - yu))

class Edge:
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end
        self.draw = False

class Poligon:
    def __init__(self, one=0, two=0, three=0):
        self.poligon = [one, two, three]

def determinant(point_list, pol):
    arr = np.array([
        [point_list[pol.poligon[0] - 1].ii, point_list[pol.poligon[0] - 1].jj, 1],
        [point_list[pol.poligon[1] - 1].ii, point_list[pol.poligon[1] - 1].jj, 1],
        [point_list[pol.poligon[2] - 1].ii, point_list[pol.poligon[2] - 1].jj, 1]
    ])
    det = np.linalg.det(arr)
    return det >= 0

def what_draw(poligon_list, edge_list, point_list):
    for i in range(len(poligon_list)):
        if not point_list[poligon_list[i].poligon[0] - 1].draw:
            point_list[poligon_list[i].poligon[0] - 1].draw = determinant(point_list, poligon_list[i])
        if not point_list[poligon_list[i].poligon[1] - 1].draw:
            point_list[poligon_list[i].poligon[1] - 1].draw = determinant(point_list, poligon_list[i])
        if not point_list[poligon_list[i].poligon[2] - 1].draw:
            point_list[poligon_list[i].poligon[2] - 1].draw = determinant(point_list, poligon_list[i])

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption('Куб Воланда')
clock = pygame.time.Clock()
rotate = True  # Changed to rotate automatically
# Reading data from file (assuming proper file format and content)
with open('coordinates.txt', 'r') as file:
    lines = file.readlines()
    n_point = int(lines[0])
    points = [Point(*list(map(float, line.split()))) for line in lines[1:n_point + 1]]
    n_edge = int(lines[n_point + 1])
    edges = [Edge(*list(map(int, line.split()))) for line in lines[n_point + 2:n_point + 2 + n_edge]]
    n_poligon = int(lines[n_point + 2 + n_edge])
    polygons = [Poligon(*list(map(int, line.split()))) for line in lines[n_point + 3 + n_edge:]]

running = True
alfi, phi = 0, 0
p = 400

while True:
    clock.tick(60)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    if rotate:
        alfi += 0.02
        phi += 0.02
    for point in points:
        point.set_view_coord(alfi, phi, p)
        point.set_screen_coords(p)
    what_draw(polygons, edges, points)
    screen.fill((0, 0, 0))
    for poligon in polygons:
        if all([points[poligon.poligon[i] - 1].draw for i in range(3)]):
            pygame.draw.polygon(screen, (255, 0, 255), [(points[poligon.poligon[i] - 1].ii, points[poligon.poligon[i] - 1].jj) for i in range(3)])
    for edge in edges:
        if points[edge.start - 1].draw and points[edge.end - 1].draw:
            start = points[edge.start - 1]
            end = points[edge.end - 1]
            pygame.draw.line(screen, (200, 43, 0), (start.ii, start.jj), (end.ii, end.jj), 3)
    pygame.display.flip()
    pygame.time.wait(10)
pygame.quit()
