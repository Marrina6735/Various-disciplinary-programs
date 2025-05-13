#include <iostream>
#include "Field.h"
#ifndef FIELD
#define FIELD
using namespace std;

class Unit {
public:
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

class Rook : public Unit {
public:
	int x = 5, y = 5;
	int coin = 0, hp = 3;
	int GetX() {
		return x;
	}

	int GetY() {
		return y;
	}

	bool is_alive() {
		return hp > 0;
	}

	int New_X(char key) {
		int dx = 0;
		switch (key) {
		// ¬верх, вниз, влево, вправо
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

	int New_Y(char key) {
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
		int nx = 0, ny = 0;
		nx = New_X(key);
		ny = New_Y(key);
		if (field->Can_Go(nx, ny)) {
			x = nx;
			y = ny;
		}
		if (field->collect_coin(nx, ny)) {
			coin++;
		}
		if (field->it_hurts(nx, ny)) {
			hp -= 1;
		}
	}

	Rook(Field* field, char symbol) :Unit(field, symbol) {
		this->field = field;
		this->symbol = symbol;
	}

	void output() {
		cout << "Health: " << hp << endl;
		cout << "Coin: " << coin << endl;
	}
};

class Bishop : public Unit {
public:
	int x = 5, y = 5;
	int coin = 0, hp = 3;
	int GetX() {
		return x;
	}

	int GetY() {
		return y;
	}

	bool is_alive() {
		return hp > 0;
	}

	int New_X(char key) {
		int dx = 0;
		switch (key) {
		// ƒвижени€ по диагонали
		case 'u':
			dx = -1;
			break;
		case 'o':
			dx = 1;
			break;
		case 'j':
			dx = -1;
			break;
		case 'l':
			dx = 1;
			break;
		}
		return x + dx;
	}

	int New_Y(char key) {
		int dy = 0;
		switch (key) {
		case 'u':
			dy = -1;
			break;
		case 'o':
			dy = -1;
			break;
		case 'j':
			dy = 1;
			break;
		case 'l':
			dy = 1;
			break;
		}
		return y + dy;
	}

	void move(char key) {
		int nx = 0, ny = 0;
		nx = New_X(key);
		ny = New_Y(key);
		if (field->Can_Go(nx, ny)) {
			x = nx;
			y = ny;
		}
		if (field->collect_coin(nx, ny)) {
			coin++;
		}
		if (field->it_hurts(nx, ny)) {
			hp -= 1;
		}
	}

	Bishop(Field* field, char symbol) :Unit(field, symbol) {
		this->field = field;
		this->symbol = symbol;
	}

	void output() {
		cout << "Health points: " << hp << endl;
		cout << "Coins: " << coin << endl;
	}
};

#endif FIELD