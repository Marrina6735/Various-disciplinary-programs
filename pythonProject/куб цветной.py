import numpy as np
import matplotlib.pyplot as plt

def draw_polygon(ax, X, Y, Z):
    ax.plot(X + [X[0]], Y + [Y[0]], Z + [Z[0]], color='black')

def scanline_fill(ax, X, Y, Z, z_buffer):
    ymin = min(Y)
    ymax = max(Y)

    for y in range(ymin, ymax + 1):
        intersections = []
        for i in range(len(X)):
            x1, y1, z1 = X[i], Y[i], Z[i]
            x2, y2, z2 = X[(i + 1) % len(X)], Y[(i + 1) % len(X)], Z[(i + 1) % len(X)]

            if (y1 <= y < y2) or (y2 <= y < y1):
                if y1 != y2:  # Избегаем деления на ноль для горизонтальных ребер
                    x = int(x1 + (y - y1) / (y2 - y1) * (x2 - x1))
                    z = z1 + (y - y1) / (y2 - y1) * (z2 - z1)
                    intersections.append((x, z))

        intersections.sort(key=lambda tup: tup[0])

        for i in range(0, len(intersections), 2):
            for x in range(intersections[i][0], intersections[i + 1][0] + 1):
                if intersections[i][0] != intersections[i + 1][0]:  # Избегаем деления на ноль для горизонтальных ребер
                    z = intersections[i][1] + (x - intersections[i][0]) / (intersections[i + 1][0] - intersections[i][0]) * (intersections[i + 1][1] - intersections[i][1])
                    if z > z_buffer[x, y]:
                        z_buffer[x, y] = z
                        ax.plot(x, y, z, 'bo', markersize=1)

def main():
    # Ваши координаты вершин многоугольников
    X1 = [100, 200, 300, 200]
    Y1 = [100, 200, 100, 50]
    Z1 = [0, 0, 0, 0]

    X2 = [200, 300, 400, 300]
    Y2 = [100, 200, 100, 50]
    Z2 = [10, 10, 10, 10]

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    z_buffer = np.full((500, 500), -np.inf)

    # Рисуем первый многоугольник
    draw_polygon(ax, X1, Y1, Z1)

    # Закрашиваем первый многоугольник
    scanline_fill(ax, X1, Y1, Z1, z_buffer)

    # Рисуем второй многоугольник
    draw_polygon(ax, X2, Y2, Z2)

    # Закрашиваем второй многоугольник
    scanline_fill(ax, X2, Y2, Z2, z_buffer)

    # Отображаем результат
    plt.show()

if __name__ == "__main__":
    main()
