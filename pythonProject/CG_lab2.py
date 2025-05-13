import matplotlib.pyplot as plt
from math import cos, sin, radians

class Cube:
    def __init__(self):
        self.vertices = [
            (-0.5, 0.5, 0.5),
            (-0.5, -0.5, 0.5),
            (-0.5, -0.5, -0.5),
            (-0.5, 0.5, -0.5),
            (0.5, 0.5, 0.5),
            (0.5, -0.5, 0.5),
            (0.5, -0.5, -0.5),
            (0.5, 0.5, -0.5)
        ]

        # Задаем ребра куба
        self.edges = [
            (0, 1), (1, 2), (2, 3), (3, 0),
            (4, 5), (5, 6), (6, 7), (7, 4),
            (0, 4), (1, 5), (2, 6), (3, 7)
        ]

        self.angle_x = 0
        self.angle_y = 0
        self.angle_z = 0

        self.fig = plt.figure()
        self.fig.canvas.mpl_connect('key_press_event', self.on_key_press)
        self.ax = self.fig.add_subplot(projection='3d')
        self.ax.set_axis_off()

    def rotate(self):
        self.ax.cla()
        self.ax.set_axis_off()
        # Матрица поворота по оси X
        rotation_x = [
            [1, 0, 0],
            [0, cos(radians(self.angle_x)), sin(radians(self.angle_x))],
            [0, -sin(radians(self.angle_x)), cos(radians(self.angle_x))]
        ]

        # Матрица поворота по оси Y
        rotation_y = [
            [cos(radians(self.angle_y)), 0, sin(radians(self.angle_y))],
            [0, 1, 0],
            [-sin(radians(self.angle_y)), 0, cos(radians(self.angle_y))]
        ]

        # Матрица поворота по оси Z
        rotation_z = [
            [cos(radians(self.angle_z)), sin(radians(self.angle_z)), 0],
            [-sin(radians(self.angle_z)), cos(radians(self.angle_z)), 0],
            [0, 0, 1]
        ]

        rotation_matrix = self.multiply_matrices(rotation_x, rotation_y)
        rotation_matrix = self.multiply_matrices(rotation_matrix, rotation_z)

        # Проходим по всем вершинам куба и применяем матрицу поворота
        rotated_vertices = []
        for vertex in self.vertices:
            rotated_vertex = [
                vertex[0] * rotation_matrix[0][0] + vertex[1] * rotation_matrix[0][1] + vertex[2] * rotation_matrix[0][
                    2],
                vertex[0] * rotation_matrix[1][0] + vertex[1] * rotation_matrix[1][1] + vertex[2] * rotation_matrix[1][
                    2],
                vertex[0] * rotation_matrix[2][0] + vertex[1] * rotation_matrix[2][1] + vertex[2] * rotation_matrix[2][
                    2]
            ]
            rotated_vertices.append(rotated_vertex)


        for edge in self.edges:
            x = [rotated_vertices[edge[0]][0], rotated_vertices[edge[1]][0]]
            y = [rotated_vertices[edge[0]][1], rotated_vertices[edge[1]][1]]
            z = [rotated_vertices[edge[0]][2], rotated_vertices[edge[1]][2]]
            self.ax.plot(x, y, z, color="black")
        plt.show()

    # Перемножаем матрицы поворота
    def multiply_matrices(self, mat1, mat2):
        result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
        for i in range(3):
            for j in range(3):
                for k in range(3):
                    result[i][j] += mat1[i][k] * mat2[k][j]
        return result

    # Функция обработки нажатий клавиш
    def on_key_press(self, event):
        key = event.key
        if key == "left":
            self.angle_y += 5
        elif key == "right":
            self.angle_y -= 5
        elif key == "up":
            self.angle_x += 5
        elif key == "down":
            self.angle_x -= 5
        elif key == "a":
            self.angle_z += 5
        elif key == "d":
            self.angle_z -= 5
        self.rotate()

    def run(self):
        self.rotate()


cube = Cube()
cube.run()