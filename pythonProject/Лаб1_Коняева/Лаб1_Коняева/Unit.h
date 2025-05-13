
#pragma once
#include <iostream>
#include "Field.h"
using namespace std;

class Unit {
	public:
	int x = 0, y = 0;
	int score = 0, hp = 3;
	Field* field;

	void move(char key);
	Unit(Field * field, char*);
};

class Rook : public Unit {
	Field* field;

	void move(char key) {
		int dx = 0, dy = 0;
		switch (key) {
		case 'w':
			dy = 1;
			break;
		case 's':
			dy = -1;
			break;
		case 'a':
			dx = -1;
			break;
		case 'd':
			dx = 1;
			break;
		case 'u':
			dy = 1;
			dx = -1;
			break;
		case 'o':
			dy = 1;
			dx = 1;
			break;
		case 'j':
			dy = -1;
			dx = -1;
			break;
		case 'l':
			dy = -1;
			dx = 1;
			break;
		}

		if (field->Can_Go(x + dx, y + dy)) {
			x += dx;
			y += dy;
		}
	}
	Unit(Field* field, char*) {
		this->field;

	}
};
class Bishop : public Unit {
	Field* field;
	void move(char key) {
		int dx = 0, dy = 0;
		switch (key) {
		case 'u':
			dy = 1;
			dx = -1;
			break;
		case 'o':
			dy = 1;
			dx = 1;
			break;
		case 'j':
			dy = -1;
			dx = -1;
			break;
		case 'l':
			dy = -1;
			dx = 1;
			break;
		}

		if (field->Can_Go(x + dx, y + dy)) {
			x += dx;
			y += dy;
		}
	}
	Unit(field, char*) {
		this->field;
	}
};
