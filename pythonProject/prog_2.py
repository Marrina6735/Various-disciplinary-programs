import math

def newtonPolynomial(x, y, n, xx): # полином Ньютона
    sum = y[0]
    for s in range(1, n): # вычисление разделенных разностей
        sigma = 0 # сумма сигма
        for j in range(0, s+1):
            q = 1
            for i in range(0, s+1): # y[i] разделенные на q c переменной сигма
                if i != j:
                    q *= (x[j] - x[i])
            sigma += y[j] / q
        for k in range(0, s):
            sigma *= (xx - x[k])
        sum += sigma
    return sum

a = 0 # начало отрезка
b = 2 # конец отрезка
N = 10 # количество частей
M = 3 * N
dx_1 = (b - a) / N # размер каждого интервала
dx_2 = (b - a) / M

# Создание списков для хранения значений x, y, N = 10
mas1_x = [0] * (N + 1)
mas1_y = [0] * (N + 1)

print("x", "\t\t", "f(x)")

# Заполнение списков значениями функции (sqrt(x) - x)
for i in range(0, N+1):
    mas1_x[i] = a + i * dx_1
    mas1_y[i] = math.sqrt(mas1_x[i]) - mas1_x[i]
    print(mas1_x[i], "\t\t", mas1_y[i])

# Создание списков для хранения значений x, y
mas2_x = [0] * (M + 1)
mas2_y = [0] * (M + 1)

print("\nx", "\t\t", "f(x)")

# Вывод значений функции в точках отрезка с более малым шагом
for i in range(0, M+1):
    mas2_x[i] = a + i * dx_2
    mas2_y[i] = math.sqrt(mas2_x[i]) - mas2_x[i]
    print(mas2_x[i], "\t\t", mas2_y[i])

print("\nResult of Newton for M = 3N")
print("x", "\t\t", "f(x)", "\t\t", "P", "\t\t", "Delta")

for i in range(0, M+1):
    P = newtonPolynomial(mas1_x, mas1_y, N + 1, mas2_x[i])
    print(mas2_x[i], "\t\t", mas2_y[i], "\t\t", P, "\t\t", abs(P - mas2_y[i]))

print("\nTask #6")

for N in range(1, 101):
    M = 3 * N
    DX1 = (b - a) / N # размер каждого интервала
    DX2 = (b - a) / M
    MAS1_x = [0] * (N + 1)
    MAS1_y = [0] * (N + 1)
    MAS2_x = [0] * (M + 1)
    MAS2_y = [0] * (M + 1)
    for j in range(0, N+1):
        MAS1_x[j] = a + j * DX1
        MAS1_y[j] = math.sqrt(MAS1_x[j]) - MAS1_x[j]
    for i in range(0, M+1):
        MAS2_x[i] = a + i * DX2
        MAS2_y[i] = math.sqrt(MAS2_x[i]) - MAS2_x[i]

    Delta = [0] * (M + 1)
    for h in range(0, M+1):
        newton = newtonPolynomial(MAS1_x, MAS1_y, N + 1, MAS2_x[h])
        Delta[h] = abs(newton - MAS2_y[h])

    count = 0.0
    for k in range(0, M+1):
        if Delta[k] > 0.1:
            break
        else:
            count += 1
    if count >= M:
        print("Answer N =", N)
        break

    del MAS1_x
    del MAS1_y
    del MAS2_x
    del MAS2_y
    del Delta

del mas1_x
del mas1_y
del mas2_x
del mas2_y



