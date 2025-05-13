#include <iostream>
using namespace std;

int main() {
	int a[10];
	int stud;
	cin >> stud; // ввод студ.билета
	for ( int i = 10 - 1; i >= 0; i--) { // заполнение массива
		a[i] = stud % 10;
		stud /= 10;
	}
	for (int i = 0; i < 10 -1; i++) { // сортировка массива по убыванию
		for (int j = i + 1; j < 10; j++) {
			if (a[i] < a[j]) {
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}
	int matrix [10][10]; // ввод матрицы
	for (int i=0; i<10; i++) { // заполнение первой строки матрицы
		matrix[0][i]=a[i];
	}

	for (int i=1; i<10; i++) { //заполнение матрицы
		for (int j=0; j<9; j++) {
			matrix[i][j] = matrix[i-1][j+1];
		}
		matrix[i][9]=matrix[i-1][0];
	}
		for (int i=0; i<=9; i++) { // вывод матрицы
			for (int j=0; j<=9; j++) {
				cout << matrix[i][j] << " ";
			}
			cout << endl;
		}
	return 0;
}
