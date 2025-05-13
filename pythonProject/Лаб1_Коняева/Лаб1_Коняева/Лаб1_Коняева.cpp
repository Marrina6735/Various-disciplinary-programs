#include <iostream>
// main file

#include <stdio.h>
#include "Field.h"
#include "Unit.h"
using namespace std;

char key;

Unit* unit;

int main() {
	srand(time(0));
	Field field(10, 10);
	field.fill();
	field.output();
	Unit* unit = new Unit(&field, "_");
	cin >> key;
	move(key);
	system("cls");
	unit = new Unit(&field, "_");
	field.output();
	return 0;
}


