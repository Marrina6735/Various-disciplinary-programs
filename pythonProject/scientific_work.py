import numpy as np
import matplotlib.pyplot as plt

def runge_kutta_step(f, y, h, t): # f - функция, описывающая систему уравнений,
                                  # y - текущее состояние системы,
                                  # h - шаг времени,
                                  # t - текущее время
    k1 = h * f(t, y)
    k2 = h * f(t + h/2, y + k1/2)
    k3 = h * f(t + h/2, y + k2/2)
    k4 = h * f(t + h, y + k3)
    return y + (k1 + 2*k2 + 2*k3 + k4)/6

def initial_problem(t, y): # функция начальных условий
    x1, y1, x2, y2, u1, v1, u2, v2, r, rho = y
    return np.array([
        u1,
        v1,
        u2,
        v2,
        (x2 - x1) * rho / r**2,
        (y2 - y1) * rho / r**2,
        (x1 - x2) * rho / r**2,
        (y1 - y2) * rho / r**2,
        1/r * ((x1 - x2)*(u1 - u2) + (y1 - y2)*(v1 - v2)),
        -rho/r**2 * ((x1 - x2)*(u1 - u2) + (y1 - y2)*(v1 - v2))
    ])

def simulate_motion(initial_values, num_steps, delta_t): # initial_values - начальные условия,
                                                         # num_steps - количество шагов,
                                                         # delta_t - временной шаг
    t_values = np.arange(0, num_steps * delta_t, delta_t)
    result = np.zeros((num_steps, len(initial_values)))

    current_values = np.array(initial_values)

    for i, t in enumerate(t_values):
        result[i, :] = current_values
        current_values = runge_kutta_step(initial_problem, current_values, delta_t, t)

    return result

# Начальные условия
initial_conditions = [0, 0, 1, 0, 0, 0, 0, 1, 1, 1]

# Моделирование движения с фиксированным временным шагом 0,001
num_steps = 100000
delta_t = 0.1
trajectory = simulate_motion(initial_conditions, num_steps, delta_t)

# Построим каждую точку в течение моделирования и проверим образование элипса
plt.plot(trajectory[:, 0] - trajectory[:, 2], trajectory[:, 1] - trajectory[:, 3])

plt.xlabel('x1 - x2')
plt.ylabel('y1 - y2')
plt.title('Не адаптивный метод Рунге-Кутты')
# plt.axis([-5, 5, -5, 5])
plt.show()