import pygame

def draw_polygon(screen, vertices, edges, color):
    n = len(vertices)
    ymin = min(vertices, key=lambda vertex: vertex[1])[1]
    ymax = max(vertices, key=lambda vertex: vertex[1])[1]

    active_edges = []
    for y in range(ymin, ymax + 1):
        intersections = []
        for i, (x1, y1, _) in enumerate(vertices):
            x2, y2, _ = vertices[edges[i][1]]

            if y1 <= y < y2 or y2 <= y < y1:
                if y1 != y2:
                    x_inter = x1 + (y - y1) * (x2 - x1) / (y2 - y1)
                    intersections.append(x_inter)

        intersections.sort()
        for i in range(0, len(intersections), 2):
            x1, x2 = int(intersections[i]), int(intersections[i + 1])
            pygame.draw.line(screen, color, (x1, y), (x2, y))

def main():
    pygame.init()
    width, height = 800, 800
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Закраска многоугольников')

    vertices1_data = [
        (50, 150, 500),
        (600, 150, 500),
        (350, 500, 300)
    ]

    edges1_data = [
        (0, 1),
        (1, 2),
        (2, 0)
    ]

    vertices2_data = [
        (200, 50, 450),
        (500, 50, 450),
        (200, 600, 450)
    ]

    edges2_data = [
        (0, 1),
        (0, 2),
        (1, 2)
    ]

    vertices1 = [(x, y) for x, y, _ in vertices1_data]
    vertices2 = [(x, y) for x, y, _ in vertices2_data]

    draw_polygon(screen, vertices1, edges1_data, (255, 0, 0))
    draw_polygon(screen, vertices2, edges2_data, (0, 0, 255))

    pygame.display.flip()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

if __name__ == "__main__":
    main()
    pygame.quit()
