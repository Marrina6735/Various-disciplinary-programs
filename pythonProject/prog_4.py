import math

def f(x, y):
    return y * math.sin(x)

def eulerMethod(a, b, y0, N):
    h = (b - a) / N
    x = a
    y = y0

    print("x\t\t\t y\t\t\t y_analytical\t\t error")
    for i in range(N+1):
        y_analytical = math.exp(1 - math.cos(x)) # analytical solution
        error = abs(y_analytical - y)
        print(f"{x}\t\t {y}\t\t {y_analytical}\t\t {error}")
        y += h * f(x, y)
        x += h

a = 0
b = 1
y0 = 1
N = 32

eulerMethod(a, b, y0, N)

for i in range(2, 101):
    Delta = [0] * i
    h = (b - a) / i
    x = a
    y = y0

    for j in range(i):
        y_analytical = math.exp(1 - math.cos(x))
        error = abs(y_analytical - y)
        Delta[j] = error
        y += h * f(x, y)
        x += h

    count = sum(1 for e in Delta if e < 0.01)
    if count == i:
        print("\nTask#3")
        print(f"N = {i}")
        print("error")
        for e in Delta:
            print(e)
        break