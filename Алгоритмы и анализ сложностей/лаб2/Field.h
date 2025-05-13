#include <stdlib.h>
#include <iostream>
using namespace std;

class Field {
public:
	char** matrix;
	int W, H;
	// ����������� ����
	Field(int W, int H) { 
		this -> W = W;
		this -> H = H;
		matrix = new char* [W];
		for (int i = 0; i < H; i++) {
			matrix[i] = new char[H];
		}
	}

	// ������� ��� ���������� �������
	void fill() { 
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				int rng = rand() % 100;
				if (rng < 50)
					// ������ (������ �����)
					matrix[i][j] = '_'; 
				else if (rng < 70)
					// �����
					matrix[i][j] = '|'; 
				else if (rng < 85) 
					// ������
					matrix[i][j] = '$';
				else
					// �������
					matrix[i][j] = 'x'; 
			}
		}
	}

	// ������� ��� ������
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

	// M������ �����
	int** matrix_weigt() {
		int** matrix_w = new int* [W];
		for (int i = 0; i < W; i++) {
			matrix_w[i] = new int[H];
			for (int j = 0; j < H; j++) {
				if (matrix[i][j] == '_')
					matrix_w[i][j] = 1;
				if (matrix[i][j] == '|')
					matrix_w[i][j] = -1;
				if (matrix[i][j] == '*')
					matrix_w[i][j] = 15;
				if (matrix[i][j] == '$')
					matrix_w[i][j] = 2;
			}
		}
		return matrix_w;
	} 

	// B���� ������� �����, �������� 
	void output_m_w(int x, int y) {
		for (int i = 0; i < W; i++) {
			for (int j = 0; j < H; j++)
				if (i == x and y == j)
					cout << '@' << ' ';
				else
					cout << matrix_weigt()[i][j] << ' ';
			cout << endl;
		}
	}
};
