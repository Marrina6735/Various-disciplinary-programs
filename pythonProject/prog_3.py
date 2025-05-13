import math

def f(x):
    return math.sqrt(x) # определение функции

def F(x):
    return (2 * x * math.sqrt(x)) / 3 # первообразная функция

def integral(a, b): # вычисление интеграла с использованием первообразной
    return F(b) - F(a)

def simpson_method(a, b, n):
    h = (b - a) / n # шаг интегрирования
    result = 0.0
    for i in range(n + 1): # вычисление значений функции в точках Х0, Х1, Х2
        x = a + i * h
        fx = f(x)
        if i == 0 or i == n:
            result += fx
        elif i % 2 == 0:
            result += 2 * fx
        else:
            result += 4 * fx
    result *= h / 3.0 # умножение суммы на шаг h/3
    return result

def trapezoid_method(a, b, n):
    h = (b - a) / n
    sum = 0.0
    for i in range(1, n):
        x = a + i * h
        sum += f(x)
    sum += (f(a) + f(b)) / 2
    result = sum * h
    return result

def right_rectangle_method(a, b, n): # метод правых прямоугольников
    h = (b - a) / n # шаг интегрирования
    result = 0.0 # вычисление суммы значений функции на правых концах прямоугольников
    for i in range(1, n + 1):
        x = a + i * h
        result += f(x)
    result *= h
    return result

def left_rectangle_method(a, b, n): # функция для вычисления интеграла методом левых прямоугольников
    h = (b - a) / n
    sum = 0
    for i in range(n):
        x = a + i * h # левая граница прямоугольника
        sum += f(x)
    result = h * sum
    return result

def main():
    a = 0 # начало отрезка
    b = 1 # конец отрезка
    N = 16 # количество частей
    methods = [integral, left_rectangle_method, right_rectangle_method, trapezoid_method, simpson_method]
    settings = [(a, b), (a, b, N), (a, b, 2 * N), (a, b, 5 * N), (a, b, 10 * N)]

    for func in methods:
        for params in settings:
            print()
        print()

    print("\nTask#3")
    for M in range(1, 100):
        I = integral(a, b)
        result = left_rectangle_method(a, b, M)
        error = abs(I - result)
        temp = 0.01
        if error < temp:
            for N in range(M - 2, M + 2):
                print(
                    f"{N}\t\t{I:.10f}\t\t{left_rectangle_method(a, b, N):.10f}\t\t{abs(I - left_rectangle_method(a, b, N)):.10f}")
            break

    print("\nTask#4")
    for M in range(1, 100):
        I = integral(a, b)
        result = right_rectangle_method(a, b, M)
        error = abs(I - result)
        temp = 0.01
        if error < temp:
            for N in range(M - 2, M + 2):
                print(
                    f"{N}\t\t{I:.10f}\t\t{right_rectangle_method(a, b, N):.10f}\t\t{abs(I - right_rectangle_method(a, b, N)):.10f}")
            break

    print("\nTask#5")
    for M in range(1, 100):
        I = integral(a, b)
        result = trapezoid_method(a, b, M)
        error = abs(I - result)
        temp = 0.01
        if error < temp:
            for N in range(M - 2, M + 2):
                print(
                    f"{N}\t\t{I:.10f}\t\t{trapezoid_method(a, b, N):.10f}\t\t{abs(I - trapezoid_method(a, b, N)):.10f}")
            break

    print("\nTask#6")
    for M in range(1, 100):
        I = integral(a, b)
        result = simpson_method(a, b, M)
        error = abs(I - result)
        temp = 0.01
        if error < temp:
            for N in range(M - 2, M + 2):
                print(f"{N}\t\t{I:.10f}\t\t{simpson_method(a, b, N):.10f}\t\t{abs(I - simpson_method(a, b, N)):.10f}")
            break


if __name__ == "__main__":
    main()
