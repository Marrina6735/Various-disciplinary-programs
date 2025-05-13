#pragma once
#include <stdlib.h>
#include <iostream>
using namespace std;

class Field {
	char ** matrix;
	int W, H;
	
public:
	Field(int W, int H) { 
		this -> W = W;
		this -> H = H;
		matrix = new char* [W];
		for (int i = 0; i < H; i++) {
			matrix[i] = new char[H];
		}
	}

	void fill() { 
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				int rng = rand() % 100;
				if (rng < 50)
					matrix[i][j] = '_'; 
				else if (rng < 70)
					matrix[i][j] = '|'; 
				else if (rng < 85)
					matrix[i][j] = '$'; 
				else
					matrix[i][j] = 'x'; 
			}
		}
	}
	void output() { 
		for (int i = 0; i < H; i++) {
			for (int j = 0; j < W; j++) {
				cout << matrix[i][j] << " ";
			}
			cout << endl;
		}
	}
	bool Can_Go(int x, int y) {
		if (x < 0 || x >= W || y < 0 || y >= H)
			return false;
		return matrix[x][y] != '|';
	}
};