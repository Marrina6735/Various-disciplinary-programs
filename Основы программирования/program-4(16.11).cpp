#include <iostream>
using namespace std;

int main() {
	int x = 0;
	int y = 0;
	char key;
	do {
		cin >> key;
		switch (key) {
			case 'w': y++;
			          break;
			case 's': y--;
			          break;
			case 'd': x++;
			          break;
			case 'a': x--;
			          break;
		}
		cout << x << ' '<< y;
	} while (key != 'e');
	return 0;
}
