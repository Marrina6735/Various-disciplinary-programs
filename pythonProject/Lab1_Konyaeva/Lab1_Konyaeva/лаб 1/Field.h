#include <stdlib.h>
#include <iostream>
using namespace std;

class Field {
	char** matrix;
	int W, H;

public:
	// Конструктор поля
	Field(int W, int H) {
		this->W = W;
		this->H = H;
		matrix = new char* [W];
		for (int i = 0; i < H; i++) {
			matrix[i] = new char[H];
		}
	}

	// Функция для заполнения матрицы
	void fill() {
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				int symbol = rand() % 100;
				if (symbol < 50)
					// Проход (пустое место)
					matrix[i][j] = '_';
				else if (symbol < 70)
					// Стена
					matrix[i][j] = '|';
				else if (symbol < 85)
					// Монета
					matrix[i][j] = '$';
				else
					// Ловушка
					matrix[i][j] = 'x';
			}
		}
	}

	// Функция для вывода
	void output(int x, int y) {
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				if (y == i && x == j)
					cout << "@" << " ";
				else
					cout << matrix[i][j] << " ";
			}
			cout << endl;
		}
	}

	bool Can_Go(int x, int y) {
		if (x < 0 || x >= W || y < 0 || y >= H)
			return false;
		return matrix[y][x] != '|';
	}

	bool collect_coin(int x, int y) {
		bool flag = matrix[y][x] == '$';
		if (flag)
			matrix[y][x] = '_';
		return flag;
	}

	bool it_hurts(int x, int y) {
		bool flag = matrix[y][x] == 'x';
		return flag;
	}
};