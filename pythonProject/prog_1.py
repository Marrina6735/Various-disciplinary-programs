import math

def lagrangePolynomial(x, y, n, xx): # полином Лагранжа
    l = 0.0
    for i in range(n):
        q = 1.0
        for j in range(n):
            if j != i:
                q *= (xx - x[j]) / (x[i] - x[j])
        l += y[i] * q
    return l

def main():
    a = 0 # начало отрезка
    b = 2 # конец отрезка
    N = 10 # количество частей
    M = 3 * N
    dx_1 = (b - a) / N # размер каждого интервала
    dx_2 = (b - a) / M

    # Создание списков для хранения значений x, y, N = 10
    mas1_x = []
    mas1_y = []

    # Заполнение списков значениями функции (sqrt(x) - x)
    for i in range(N+1):
        mas1_x.append(round(a + i * dx_1,2))
        mas1_y.append(math.sqrt(mas1_x[i]) - mas1_x[i])
        print("x =", mas1_x[i], "\t\ty =", mas1_y[i])

    print("\nResult for N = 10")
    for i in range(N+1):
        L1 = lagrangePolynomial(mas1_x, mas1_y, N + 1, mas1_x[i])
        print("x =", mas1_x[i], "\t\t", "f(x) =", mas1_y[i], "\t\t", "L =", L1)
    print()

    # Создание списков для хранения значений x, y
    mas2_x = []
    mas2_y = []

    # Вывод значений функции в точках отрезка с более малым шагом
    for i in range(M+1):
        mas2_x.append(a + i * dx_2)
        mas2_y.append(math.sqrt(mas2_x[i]) - mas2_x[i])
        print("x =", mas2_x[i], "\t\ty =", mas2_y[i])
    print("\nResult for M = 3N")
    for i in range(M+1):
        L = lagrangePolynomial(mas1_x, mas1_y, N + 1, mas2_x[i])
        print("x =", mas2_x[i], "\t\tf(x) =", mas2_y[i], "\t\tLagrange =", L, "\t\tDelta =", abs(L - mas2_y[i]))
    print("\nTask #6")
    for Q in range(1, 51):
        #print("N =", Q)
        R = 3 * Q
        DX1 = (b - a) / Q  # размер каждого интервала
        DX2 = (b - a) / R
        MAS1_x = []
        MAS1_y = []
        MAS2_x = []
        MAS2_y = []
        for j in range(Q+1):
            MAS1_x.append(a + j * DX1)
            MAS1_y.append(math.sqrt(MAS1_x[j]) - MAS1_x[j])
            #print("x =", MAS1_x[j], "\t\ty =", MAS1_y[j])
        #print()
        for i in range(R+1):
            MAS2_x.append(a + i * DX2)
            MAS2_y.append(math.sqrt(MAS2_x[i]) - MAS2_x[i])
            #print("x =", MAS2_x[i], "\t\ty =", MAS2_y[i])
        #print()
        Delta = []
        for h in range(R+1):
            Lagrange = lagrangePolynomial(MAS1_x, MAS1_y, Q + 1, MAS2_x[h])
            Delta.append(abs(Lagrange - MAS2_y[h]))
            #print("Delta =", Delta[h])

        count = 0.0
        for k in range(R+1):
            if Delta[k] > 0.01:
                break
            else:
                count += 1
        if count >= R:
            #print("Finish, the answer is N =", Q)
            break
    print("Finish, the answer is N =", Q)

    # Освобождение памяти
    mas1_x.clear()
    mas1_y.clear()
    mas2_x.clear()
    mas2_y.clear()

if __name__ == '__main__':
        main()
