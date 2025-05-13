#include <iostream>
using namespace std;

int main() {
	int n = 0;
	int a;
	char function;
	do {
		cout << "Введите комнаду '+', '-', '*' или '/' : " << endl;
		cin >> function;
		switch (function) {
			case '+': cin >> a; // Функция сложения
				      n = n + a;
				      cout << "n = " << n << endl;
			          break;
			case '-': cin >> a; // Функция вычитания
				      n = n - a;
				      cout << "n = " << n << endl;
			          break;
			case '*': cin >> a; // Функция умножения
				      n = n * a;
				      cout << "n = " << n << endl;
			          break;
			case '/': cin >> a; // Функция деления
				      if (a != 0) {
				          n = n / a; 
				          cout << "n = " << n << endl;
				      } else cout << "На ноль делить нельзя, выберите другую операцию " << endl;
			          break;
		}
	} while (function != 'e');
	cout << "Окончательное значение n = " << n;
	return 0;
}
