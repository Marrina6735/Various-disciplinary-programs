#include <iostream>
using namespace std;

int main() {
	int number;
	cin >> number; // ввод произвольного числа 
	int size = 0;
	int temp = number;
	while (temp > 0) { // цикл для нахождения размера масссива
		size++;
		temp /= 10;
	}	
	int* a = new int [size];
	for ( int i = size - 1; i >= 0; i--) { // заполнение массива
		a[i] = number % 10;
		number /= 10;
	}
	for (int i = 0; i < size -1; i++) { // сортировка массива по убыванию
		for (int j = i + 1; j < size; j++) {
			if (a[i] < a[j]) {
				int temp = a[i];
				a[i] = a[j];
				a[j] = temp;
			}
		}
	}
	
	int** matrix = new int* [size];
	for (int i = 0; i < size; i++) { // сегментирование матрицы
		matrix[i] = new int[size];
	}
	for (int i = 0; i < size; i++) { // заполнение первой строки матрицы
		matrix[0][i]=a[i];
	}
	for (int i = 1; i < size; i++) { //заполнение матрицы
		for (int j = 0; j < size; j++) {
			matrix[i][j] = matrix[i-1][j+1];
		}
		matrix[i][size-1] = matrix[i-1][0];
	}
		for (int i = 0; i <= size - 1; i++) { // вывод матрицы
			for (int j = 0; j <= size-1; j++) {
				cout << matrix[i][j] << " ";
			}
			cout << endl;
		}
	return 0;
}
