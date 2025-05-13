import math

def f(x, y):
    return y * math.sin(x)

def runge_kutta_2_method(a, b, y0, N):
    h = (b - a) / N
    x = a
    y = y0

    print("x\t\t\t y_numerical\t\t y_analytical\t\t error")

    for i in range(N + 1):
        y_analytical = math.exp(1 - math.cos(x))
        error = abs(y_analytical - y)
        print(f"{x:.6f}\t\t {y:.6f}\t\t {y_analytical:.6f}\t\t {error:.6f}")

        k1 = h * f(x, y)
        k2 = h * f(x + h, y + k1)

        y += 0.5 * (k1 + k2)
        x += h

def main():
    a = 0
    b = 1
    y0 = 1
    N = 32

    runge_kutta_2_method(a, b, y0, N)

    for i in range(2, 101):
        Delta = [0] * i
        h = (b - a) / i
        x = a
        y = y0

        for j in range(i):
            y_analytical = math.exp(1 - math.cos(x))
            error = abs(y_analytical - y)
            Delta[j] = error

            k1 = h * f(x, y)
            k2 = h * f(x + h, y + k1)

            y += 0.5 * (k1 + k2)
            x += h

        count = sum(1 for error in Delta if error < 0.01)

        if count == i:
            print("\nTask#3")
            print(f"ATTENTION: N = {i}")
            print("error")
            for error in Delta:
                print(error)
            break

if __name__ == "__main__":
    main()