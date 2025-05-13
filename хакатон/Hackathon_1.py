import numpy as np
from scipy.integrate import solve_ivp
from multiprocessing import Pool
import matplotlib.pyplot as plt
import time


def system(t, y, G):
    Mx, My, Mz = y
    dMx_dt = -G * Mx * Mz
    dMy_dt = G * Mx * My
    dMz_dt = G * (Mx ** 2 - My ** 2)
    return [dMx_dt, dMy_dt, dMz_dt]


def solve_ode_for_G(G, t_span, y0, N_points):
    t_eval = np.linspace(t_span[0], t_span[1], N_points)
    sol = solve_ivp(system, t_span, y0, t_eval=t_eval, args=(G,))
    return sol.t, sol.y


def find_time_of_stabilization(t, y, N_stab=100, epsilon=1e-4):
    for i in range(N_stab, len(t)):
        if np.all(np.abs(y[:, i] - np.mean(y[:, i - N_stab:i], axis=1)) < epsilon):
            return t[i]
    return t[-1]


def average_values(t, y, ts):
    mask = t >= ts
    mx_avg = np.mean(y[0, mask])
    my_avg = np.mean(y[1, mask])
    mz_avg = np.mean(y[2, mask])
    return mx_avg, my_avg, mz_avg


def compute_for_G(G, t_span, y0, N_points):
    t, y = solve_ode_for_G(G, t_span, y0, N_points)
    ts = find_time_of_stabilization(t, y)
    mx_avg, my_avg, mz_avg = average_values(t, y, ts)
    return G, mx_avg, my_avg, mz_avg


def parallel_computation(G_values, t_span, y0, N_points, num_threads):
    with Pool(num_threads) as pool:
        results = pool.starmap(compute_for_G, [(G, t_span, y0, N_points) for G in G_values])
    return results


def plot_speedup(thread_counts, times):
    plt.figure()
    plt.plot(thread_counts, times, marker='o')
    plt.xlabel("Количество потоков")
    plt.ylabel("Время вычислений (с)")
    plt.title("Зависимость времени вычислений от количества потоков")
    plt.grid(True)
    plt.show()


def plot_results(results):
    G_values, mx_avgs, my_avgs, mz_avgs = zip(*results)
    plt.figure()
    plt.plot(G_values, mx_avgs, label='<mx>')
    plt.plot(G_values, my_avgs, label='<my>')
    plt.plot(G_values, mz_avgs, label='<mz>')
    plt.xlabel("G")
    plt.ylabel("Средние значения")
    plt.title("Зависимость средних значений от G")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    G_values = np.linspace(0.1, 10, 200)
    t_span = (0, 1500)
    y0 = [1, 0, 0]
    N_points = 15000

    thread_counts = [1, 2, 4, 8]
    times = []

    for num_threads in thread_counts:
        start_time = time.time()
        results = parallel_computation(G_values, t_span, y0, N_points, num_threads)
        times.append(time.time() - start_time)

    plot_results(results)
    plot_speedup(thread_counts, times)


def average_values(t, y, ts):
    mask = t >= ts
    mx_avg = np.mean(y[0, mask])
    my_avg = np.mean(y[1, mask])
    mz_avg = np.mean(y[2, mask])
    return mx_avg, my_avg, mz_avg


t = np.linspace(0, 1500, 15000)
y = np.array([np.sin(t), np.cos(t), np.sin(2 * t)])
ts = 1000  # времяч стабилизации
mx_avg, my_avg, mz_avg = average_values(t, y, ts)
print("Среднее значение mx:", mx_avg)
print("Среднее значение my:", my_avg)
print("Среднее значение mz:", mz_avg)


def analyze_elem(arr, ii):
    summm = sum(arr[0 + ii * 100: 100 + ii * 100])
    summm = summm * 0.01
    return summm


def comparison(ii):
    return analyze_elem(sol_1.y[0], ii) - analyze_elem(sol_1.y[0], ii + 1)


itog = None

for i in range(15):
    if abs(comparison(i)) < 1e-6:
        itog = i
        break




