N = 4
k = 2
matrix = [[0, 1, 0, 1],
          [1, 0, 0, 1],
          [1, 0, 1, 0],
          [0, 1, 1, 0]]
g = [0, 1, 0, 0]
status = []
value = []
stop_masiv = []

a1 = matrix[0][1]
a2 = matrix[0][2]
b1 = matrix[1][0]
b2 = matrix[1][3]
c1 = matrix[2][1]
c2 = matrix[2][3]
d1 = matrix[3][0]
d2 = matrix[3][1]
print(matrix)
def summation(a1, a2):
    if (a1 == 1) or (a2 == 1):
        return 1
    else:
        return 0
value.append(summation(a1,a2))

def multi(b1, b2):
    return b1 * b2
value.append(multi(b1,b2))

def consecution(c1,c2):
    if ( c1 == 1) and (c2 == 0):
        return 0
    else:
        return 1
value.append(consecution(c1,c2))

def equation(d1,d2):
    if d1 == d2:
        return 1
    else:
        return 0
value.append(equation(d1,d2))
matrix.insert(0, value)
matrix.pop(1)
k0 = 0
print(matrix)

while value not in stop_masiv:
    value = []
    value.append(summation(a1,a2))
    value.append(multi(b1,b2))
    value.append(consecution(c1,c2))
    value.append(equation(d1,d2))
    if k0 == 3:
        k0 = 0
    else:
        k0 += 1
    matrix[k0] = value
    stop_masiv.append(value)
    print(value)
print("123")
i = (print(i) for i in matrix)