#include <iostream>
#include <stdio.h>
#include "Unit.h"
using namespace std;

char key;
char id_unit;

int main() {
	cout << "Your field:\n";
	srand(time(0));
	Field field(10, 10);
	field.fill();
	field.output(5, 5);
	cout << "You will be here: @\n";
	cout << "Select movements: 1 (Rook: wsad), 2 (Bishop: uojl)\n";
	cin >> id_unit;
	if (id_unit == '1') {
		cout << "Reminder:\n";
		cout << "w (up), s (down), a (left), d (right)\n";
		cout << "Press to exit: e\n";
		Rook* R = new Rook(&field, '_');
		while (key != 'e' && R->is_alive()) {
			cin >> key;
			R->move(key);
			system("cls");
			field.output(R->GetX(), R->GetY());
			R->output();
			cout << "Press to exit: e\n";
		}
		cout << "The End!";
	}
	else if (id_unit == '2') {
		cout << "Reminder:\n";
		cout << "u (diagonal up to the left), j (diagonal down to the left), o (diagonal up to the right), l (diagonal down to the right)\n";
		cout << "Press to exit: e\n";
		Bishop* B = new Bishop(&field, '_');
		while (key != 'e' && B->is_alive()) {
			cin >> key;
			B->move(key);
			system("cls");
			field.output(B->GetX(), B->GetY());
			B->output();
			cout << "Press to exit: e\n";
		}
		cout << "The End!";
	}

	return 0;
}

