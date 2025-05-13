#include <iostream>
#include "Field.h"
#ifndef FIELD
#define FIELD
using namespace std;

struct Coords {
	int x, y;
	Coords(int x, int y) {
		this->x = x;
		this->y = y;
	}
};

class Unit {
public:
	int x, y;
	Coords get_coords() {
		return Coords(x, y);
	}

	char symbol;
	Field* field;

	Unit(Field* field, char symbol) {
		this->field = field;
		this->symbol = symbol;
	};

	int virtual  GetX() = 0;
	int virtual GetY() = 0;
	bool virtual is_alive() = 0;
	int virtual New_X(char key) = 0;
	int virtual New_Y(char key) = 0;
	void virtual move(char key) = 0;
	void virtual output() = 0;
};

class Hero1: public Unit {
public:
	int x = 5, y = 5;
	int coin = 0, hp = 3;

	Unit* enemy;
	 Coords NextStep(Coords dist) {
		int** A = new int* [field -> W];
		for (int i = 0; i < field->W; i++) {
			A[i] = new int[field->H];
			for (int j = 0; j < field->H; j++) {
				A[i][j] = -2;
			}
		}
		A[y][x] = 0;
		bool flag = true;
		while (flag) {
			flag = false;
		}
		for (int i = 0; i < field->W; i++) {
			for (int j = 0; j < field->H; j++) {
				if (field->matrix_weigt()[i][j] == -1);
				if (i > 0) {
					if (A[i - 1][j] >= 0 && ((A[i - 1][j] + field->matrix_weigt()[i][j] < A[i][j]) || A[i][j] == -2)) {
						A[i][j] = A[i - 1][j] + field->matrix_weigt()[i][j];
						flag = true;
					}
					else if (i > 0) {
						if (A[i + 1][j] >= 0 && ((A[i + 1][j] + field->matrix_weigt()[i][j] < A[i][j]) || A[i][j] == -2)) {
							A[i][j] = A[i + 1][j] + field->matrix_weigt()[i][j];
							flag = true;
						}
					}
					else if (j > 0) {
						if (A[i][j - 1] >= 0 && ((A[i][j - 1] + field->matrix_weigt()[i][j] < A[i][j]) || A[i][j] == -2)) {
							A[i][j] = A[i][j - 1] + field->matrix_weigt()[i][j];
							flag = true;
						}
					}

					else if (j > 0) {
						if (A[i][j + 1] >= 0 && ((A[i][j + 1] + field->matrix_weigt()[i][j] < A[i][j]) || A[i][j] == -2)) {
							A[i][j] = A[i][j + 1] + field->matrix_weigt()[i][j];
							flag = true;
						}
					}
				}
			}			
		}  
		if (A[dist.y][dist.x] < 0) {
			return Coords(-1, -1);
		}
		while (!((dist.x == x && (dist.y == y+1 || dist.y == y-1)) || (dist.y == y && (dist.x == x+1 || dist.x == x-1))))
		{
			int up, down, left, right = -1;
			if (dist.y > 0)
			up = A[dist.y - 1][dist.x];

			if (dist.y > field->W);
			down = A[dist.y + 1][dist.x];

			if (dist.x > 0);
			left = A[dist.y][dist.x-1];

			if (dist.x > field->H);
			right = A[dist.y][dist.x + 1];

			if (up < 0)
				up = 100000;

			if (down < 0)
				down = 100000;

			if (right < 0)
				right = 100000;

			if (left < 0)
				left = 100000;

			if((up < down) and (up < left) and (up < right))
				dist.y = dist.y - 1;

			if ((down < up) and (down < left) and (down < right))
				dist.y = dist.y + 1;

			if ((left < down) and (left < up) and (left < right))
				dist.x = dist.x - 1;

			if ((right < down) and (right < left) and (right < up))
				dist.x = dist.x + 1;
			return dist;
		}
	}
	int GetX() {
		return x;
	}
	int GetY() {
		return y;
	}
	bool is_alive() {
		return hp > 0;
	}
	int new_x(char key) {
		int dx = 0;
		switch (key) {
		case 'w':
			dx = -0;
			break;
		case 's':
			dx = 0;
			break;
		case 'a':
			dx = -1;
			break;
		case 'd':
			dx = 1;
			break;
		}
		return x + dx;
	}
	int new_y(char key) {
		int dy = 0;
		switch (key) {
		case 'w':
			dy = -1;
			break;
		case 's':
			dy = 1;
			break;
		case 'a':
			dy = 0;
			break;
		case 'd':
			dy = 0;
			break;
		}
		return y + dy;
	}
	void move(char key) {
		Coords neww = NextStep(enemy->get_coords());
		int newx = new_x(key);
		int newy = new_y(key);
		if (field->Can_Go(newx, newy)) {
			x = newx;
			y = newy;
			if (field->collect_coin(x, y)) {
				coin++;
				cout << "Your account top up!" << endl;
			}
			else if (field->it_hurts(x, y)) {
				hp--;
				cout << "You fall into a trap!"<< endl;
			}
		}
	}
	Hero1(Field* field, char symbol) :Unit(field, symbol) {
		this->field = field;
		this->symbol = symbol;
	}
	void output() {
		cout << "Health: " << hp << endl;
		cout << "Coin: " << coin << endl;
	}
};

#endif FIELD