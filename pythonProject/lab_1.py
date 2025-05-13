# Для первого случая матрицы 4*4
N = 4
k = 2
print("Для матрицы 4*4, где N = 4 k = 2")
matrix_1 = [[0, 1, 0, 1],  # Матрица связи 4*4
            [1, 0, 1, 0],
            [1, 0, 0, 1],
            [0, 1, 1, 0]]

for i in matrix_1:
    print(i)
print()
length_2 = 3
g_1 = [[0, 0, 0, 0], [0, 0, 0, 1], [0, 0, 1, 0],
       [0, 0, 1, 1], [0, 1, 0, 0], [0, 1, 0, 1],
       [0, 1, 1, 0], [0, 1, 1, 1], [1, 0, 0, 0],
       [1, 0, 0, 1], [1, 0, 1, 0], [1, 0, 1, 1],
       [1, 1, 0, 0], [1, 1, 0, 1], [1, 1, 1, 0],
       [1, 1, 1, 1]]

value_1 = []


def summation(b, d):  # (А или В)
    if b == 1 or d == 1:
        return 1
    return 0


def multi(a, c):  # (А и В)
    if a == 1 and c == 1:
        return 1
    return 0


def consec(a, d):  # ( (не А) и (не В))
    if a == 0 and d == 0:
        return 1
    elif a == 1 and d == 1:
        return 0
    return 1


def unit(b, c):  # (А и (не В) или (не А) и В)
    if b == c or c == b:
        return 0
    return 1


for i in g_1:
    for j in i:
        a = i[0]
        b = i[1]
        c = i[2]
        d = i[3]
        matrix1_2 = []
        matrix = []
        matrix.append(i)
        for e in matrix:
            if matrix.count(e) > 1:
                n: int = matrix.index(e)
                m = len(matrix) - 1
                length = m - n
                break
            for f in e:
                a = e[0]
                b = e[1]
                c = e[2]
                d = e[3]
                matrix1_2 = [summation(b, d), multi(a, c), consec(a, d), unit(b, c)]
                matrix.append(matrix1_2)
                matrix1_2 = []
                break
            else:
                continue
        for t in matrix:
            print(t)
        print("length = ", length)
        print()
        break
length_1 = 9
print("average = ", length_1 / 3)
print()

# Для второго случая матрицы 5*5
N = 5
k = 3
print("Для матрицы 5*5, где N = 5 k = 3")
matrix2_1 = []
matrix_2 = [[0, 0, 1, 1, 1],  # Матрица связи 5*5
            [1, 0, 0, 1, 1],
            [1, 1, 0, 1, 0],
            [0, 1, 1, 0, 1],
            [1, 1, 1, 0, 0]]

for i in matrix_2:
    print(i)
print()
g_2 = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 1], [0, 0, 0, 1, 0], [0, 0, 0, 1, 1],
       [0, 0, 1, 0, 0], [0, 0, 1, 0, 1], [0, 0, 1, 1, 0], [0, 0, 1, 1, 1],
       [0, 1, 0, 0, 0], [0, 1, 0, 0, 1], [0, 1, 0, 1, 0], [0, 1, 0, 1, 1],
       [0, 1, 1, 0, 0], [0, 1, 1, 0, 1], [0, 1, 1, 1, 0], [0, 1, 1, 1, 1],
       [1, 0, 0, 0, 0], [1, 0, 0, 0, 1], [1, 0, 0, 1, 0], [1, 0, 0, 1, 1],
       [1, 0, 1, 0, 0], [1, 0, 1, 0, 1], [1, 0, 1, 1, 0], [1, 0, 1, 1, 1],
       [1, 1, 0, 0, 0], [1, 1, 0, 0, 1], [1, 1, 0, 1, 0], [1, 1, 0, 1, 1],
       [1, 1, 1, 0, 0], [1, 1, 1, 0, 1], [1, 1, 1, 1, 0], [1, 1, 1, 1, 1]]


def summation_2(c, d, e):  # (А или В или С)
    if c == d == e == 0:
        return 0
    return 1


def multi_2(a, d, e):  # (А и В и С)
    if a == 0 or d == 0 or e == 0:
        return 0
    return 1


def consec_2(a, b, d):
    if a == b == d == 1:
        return 0
    return 1


def unit_2(b, c, e):
    if b == c and c == b and e == 0:
        return 0
    elif b == c and c == b and e == 1:
        return 1
    elif b != c and c != b and e == 1:
        return 0
    return 1


def accor_2(a, b, c):
    if (c == 1 and a == b == 1) or (a == b == 0 and c == 1) or (a == 1 and b == 0 and c == 1 or c == 0) or (
            a == 0 and b == 1 and c == 1 or c == 0):
        return 1
    elif (a == b == 1 and c == 0) or (a == b == 0 and c == 0):
        return 0


for i in g_2:
    flag = True
    for j in i:
        mat = []
        a = i[0]
        b = i[1]
        c = i[2]
        d = i[3]
        e = i[4]
        matrix2_2 = []
        matrix2_1 = []
        matrix2_1.append(i)
        for f in matrix2_1:
            if matrix2_1.count(f) > 1:
                n: int = matrix2_1.index(f)
                m = len(matrix2_1) - 1
                length_1 = m - n
                break
            for g in f:
                a = f[0]
                b = f[1]
                c = f[2]
                d = f[3]
                e = f[4]
                matrix2_2 = [summation_2(c, d, e), multi_2(a, d, e), consec_2(a, b, d), unit_2(b, c, e),
                             accor_2(a, b, c)]
                matrix2_1.append(matrix2_2)
                matrix2_22 = matrix2_2
                matrix2_2 = []
                if matrix2_22 in mat:
                    flag = False
                if flag:
                    if matrix2_22 not in mat:
                        mat.append(matrix2_22)

                break

        for t in matrix2_1:
            print(t)
        print("length = ", length_1)
        print()

        print('_' * 300)
        break
print('Колическтво различных атракторов ', len(mat))
print("Cредняя длина ", length_2 / len(mat))
# print(len(mat))
