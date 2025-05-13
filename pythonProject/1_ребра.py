import pygame
import math

n_point, n_edge = 0, 0

class Edge:
    def __init__(self, s, e):
        self.start = s
        self.end = e

class Point:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

class Vertex2:
    def __init__(self, x, y, z):
        self.w = Point(x, y, z)
        self.e = Point(x, y, z)

    def set_view_coord(self, theta, phi, ro):
        st = math.sin(theta)
        ct = math.cos(theta)
        sf = math.sin(phi)
        cf = math.cos(phi)
        self.e.x = -st * self.w.x + ct * self.w.y
        self.e.y = -cf * ct * self.w.x - cf * st * self.w.y + sf * self.w.z
        self.e.z = -sf * ct * self.w.x - sf * st * self.w.y - cf * self.w.z + ro

    def set_screen_coords(self, ro):
        x = ro * self.e.x / (2 * self.e.z)
        y = ro * self.e.y / (2 * self.e.z)
        xr, xl, yd, yu = 500, 0, 0, 500
        ir, il, jd, ju = 500, 0, 500, 0
        self.i = il + ((x - xr) * (ir - il) / (xl - xr))
        self.j = ju + ((y - yu) * (jd - ju) / (yd - yu))

    def line_drawn(self, x1, y1, x2, y2, window):
        pygame.draw.line(window, (64, 150, 208), (x1, y1), (x2, y2))

def main():
    theta = 0
    phi = 0
    ro = 400
    path = "coordinates.txt"
    try:
        fin = open(path, "r")
        s = fin.readline()
        n_point = int(s.strip())
        mas = []
        for i in range(n_point):
            s = fin.readline()
            s = s.split()
            vertex = Vertex2(float(s[0]), float(s[1]), float(s[2]))
            mas.append(vertex)
        s = fin.readline()
        n_edge = int(s.strip())
        mas_edges = []
        for i in range(n_edge):
            s = fin.readline()
            s = s.split()
            b = Edge(int(s[0]), int(s[1]))
            mas_edges.append(b)
        fin.close()
        window_width, window_height = 1000, 1000
        window = pygame.display.set_mode((window_width, window_height))
        pygame.display.set_caption("Куб Воланда")
        clock = pygame.time.Clock()
        rotate = True  # Автоматический поворот
        while True:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
            window.fill((0, 0, 0))
            if rotate:
                theta += 0.02
                phi += 0.02
            for i in range(n_point):
                mas[i].set_view_coord(theta, phi, ro)
                mas[i].set_screen_coords(ro)
            for e in range(n_edge):
                mas[0].line_drawn(mas[mas_edges[e].start - 1].i, mas[mas_edges[e].start - 1].j,
                                  mas[mas_edges[e].end - 1].i, mas[mas_edges[e].end - 1].j, window)
            pygame.display.update()
    except IOError:
        print("Такого файла нет.")

if __name__ == "__main__":
    main()
