#include <iostream>
#include <math.h>

using namespace std;

// Обьявление эталонной функции y(x) = k1*x^3 + k2*x^2 + k3*x + k4
float k1, k2, k3, k4; // Начальные параметры
float stand;
float d_stand;
bool flag;

float function(float* prm, float x) { // Функция, заданная массивом коэффициентов k1, k2, k3, k4
    return prm[0] * pow(x, 3) + prm[1] * pow(x, 2) + prm[2] * x + prm[3];
}

float distance(float* prm, float* stand_prm, float x0, float x1, float dx) { // Прямой признак - расстояние между графиками от -100 до 100
    float summ = 0;
    for (float x = x0 + dx; x <= x1; x += dx) {
        summ += (abs(function(prm, x) - function(stand_prm, x)));
    }
    return summ;
}

float integral(float* prm, float x0, float x1, float dx) { // Косвенный признак - сравнение интеграла функции от -100 до 100
    float summ = 0;
    for (float x = x0 + dx; x <= x1; x += dx) {
        summ += (function(prm, x - dx) + function(prm, x)) / 2 * dx;
    }
    return summ;
}

class Feature {
public:
    float* prm;
    float d;
    Feature(float* prm, float max_d, bool flag) {
        this->prm = new float[4];
        for (int i = 0; i < 4; i++) {
            this->prm[i] = prm[i] + (rand() % 201 - 100) / 100.0 * max_d;
        }
        if (flag == 0)
            d = abs(stand - integral(this->prm, -100, 100, 0.5));
        else
            d = distance(this->prm, new float [4] {k1, k2, k3, k4}, -100, 100, 0.5);
    }

    void output() {
        cout << "Parameter: " << endl;
        for (int i = 0; i < 4; i++)
            cout << prm[i] << " ";
        cout << "d: " << d << endl;
    };
};

Feature generation(Feature origin, int count, float max_d, bool flag) { // Генерация поколения, позитивное изменение стремится до пренебрежимо малому значению
    Feature close = origin;
    for (int i = 0; i < count; i++) {
        Feature temp = Feature(origin.prm, max_d, flag);
        if (temp.d < close.d)
            close = temp;
    }
    return close;
}

int main() {
    int n = 0;
    k1 = 1;
    k2 = 2;
    k3 = 3;
    k4 = 4;
    cin >> flag;
    if (not flag) {
        stand = integral(new float[4] {k1, k2, k3, k4}, -100, 100, 0.5);
        cout << "Standard: " << stand << endl;
        Feature f(new float[4] {0.4, 0.5, 0.6, 0.5}, 0.5, 0);
        while (f.d > 100000) {
            Feature gen = generation(f, 100, 0.5, 0);
            f = gen;
            f.output();
        }
    }
    else {
        cout << "Standard: " << d_stand << endl;
        Feature d_f(new float[4] {0.4, 1.5, 2.6, 0.5}, 0.5, 1);
        while (d_f.d > 1000) {
            Feature gen = generation(d_f, 100, 0.5, 1);
            d_f = gen;
            d_f.output();
        }
    }
    return 0;
}
