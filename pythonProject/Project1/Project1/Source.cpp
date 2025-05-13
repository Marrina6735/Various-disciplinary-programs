#include <iostream>
#include <windows.h>
#include <vector>

using namespace std;
class As {
public:
	float RAZA[100]; //векторы разностей координат нового объекта с координатами ядер соответствующего класса
	float SOVA[100]; //вектор результата умножения координат нового объекта на обратную матрицу ковариации
	float CA[100]; //ядра классов 1-3
	float COVA[100][100]; //матрицы ковариации классов 1-3
	float final1 = 0;
};
class Bs {
public:
	float RAZB[100]; 
	float SOVB[100]; 
	float CB[100]; 
	float COVB[100][100]; 
	float final2 = 0;
};
class Cs {
public:
	float RAZC[100]; 
	float SOVC[100]; 
	float CC[100]; 
	float COVC[100][100]; 
	float final3 = 0;
};

void E_A(float M[100][100]) { //функция, необходимая дли нахождения обратной матрицы ковариации
	double t;
	int E[100][100];
	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 100; j++) {
			E[i][j] = 0.0;
			if (i == j) { E[i][j] = 1.0; }
		}
	for (int a = 0; a < 100; a++) {
		t = M[a][a];
		for (int b = 0; b < 100; b++) {
			M[a][b] = M[a][b] / t;
			E[a][b] = E[a][b] / t;
		}
		for (int i = a + 1; i < 100; i++) {
			t = M[i][a]; 
			for (int b = 0; b < 100; b++) 
			{
				M[i][b] = M[i][b] - M[a][b] * t;
				E[i][b] = E[i][b] - E[a][b] * t;
			}
		}
	}

	for (int a = 99; a > 0; a--) 
	{
		for (int i = a - 1; i >= 0; i--) 
		{
			t = M[i][a];//сохраняя первый элемент, идущий после элемента главной диагонали данной строки
			for (int b = 0; b < 100; b++) {
				M[i][b] = M[i][b] - M[a][b] * t;
				E[i][b] = E[i][b] - E[a][b] * t;
			}
		}
	}
	for (int i = 0; i < 100; i++) { // E = A^(-1)
		for (int b = 0; b < 100; b++) {
			M[i][b] = E[i][b];
		}
	}
}

int main() {
	As Ac;
	Bs Bc;
	Cs Cc;
	string start = "";
	float A[100]; 
	float B[100];
	float C[100];
	vector <string> pic; 
	for (int step = 0; step < 3; step++) {
		cout << "Enter three objects of the class " << step + 1 << " (10 x 10)" << endl; // (3 раза: для 3-х представителей класса)
		for (int i = 0; i < 10; i++) {
			cin >> start;
			pic.push_back(start);
			for (int j = 0; j < 10; j++) {
				A[10 * i + j] = start[j] - 48; 
				if (start[j] - 48 == 0) { pic[i][j] = ' '; }//если это был 0, то выводим пробел
				else (pic[i][j] = char(219));//иначе выводим прямоугольник
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				cout << pic[i][j];//выводим комбинацию для визуального представления объектов
			}
			cout << endl;
		}
		cout << endl;
		pic.clear();
		for (int i = 0; i < 10; i++) {
			cin >> start;
			for (int j = 0; j < 10; j++) {
				pic.push_back(start);
				B[10 * i + j] = start[j] - 48;
				if (start[j] - 48 == 0) { pic[i][j] = ' '; }
				else (pic[i][j] = char(219));
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				cout << pic[i][j];
			}
			cout << endl;
		}
		cout << endl;
		pic.clear();
		for (int i = 0; i < 10; i++) {
			cin >> start;
			for (int j = 0; j < 10; j++) {
				pic.push_back(start);
				C[10 * i + j] = start[j] - 48;
				if (start[j] - 48 == 0) { pic[i][j] = ' '; }
				else (pic[i][j] = char(219));
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				cout << pic[i][j];
			}
			cout << endl;
		}
		cout << endl;
		pic.clear();
		for (int i = 0; i < 100; i++) {
			if (step == 0) { Ac.CA[i] = (A[i] + B[i] + C[i]) / 3; } // ядро соответствующего класса
			if (step == 1) { Bc.CB[i] = (A[i] + B[i] + C[i]) / 3; }
			if (step == 2) { Cc.CC[i] = (A[i] + B[i] + C[i]) / 3; }

		}
		for (int i = 0; i < 100; i++) {//зная координаты ядра и представителей класса
			for (int j = 0; j < 100; j++) {
				if (step == 0) {
					Ac.COVA[i][j] = 1 / 2.0 * ((A[i] - Ac.CA[i]) * (A[j] - Ac.CA[j]) + (B[i] - Ac.CA[i]) * (B[j] - Ac.CA[j]) + (C[i] - Ac.CA[i]) * (C[j] - Ac.CA[j])); //находим элементы матрицы ковариации
					if (i == j) { Ac.COVA[i][j]++; }//прибавляем единицы к элементам главной диагонали (+Е, чтобы избежать обнуление элементов главной диагонали)
				}//на каждом этапе вычисляем соответствующую матрицу ковариации
				if (step == 1) {
					Bc.COVB[i][j] = 1 / 2.0 * ((A[i] - Bc.CB[i]) * (A[j] - Bc.CB[i]) + (B[i] - Bc.CB[i]) * (B[j] - Bc.CB[i]) + (C[i] - Bc.CB[i]) * (C[j] - Bc.CB[i]));
					if (i == j) { Bc.COVB[i][j]++; }
				}
				if (step == 2) {
					Cc.COVC[i][j] = 1 / 2.0 * ((A[i] - Cc.CC[i]) * (A[j] - Cc.CC[j]) + (B[i] - Cc.CC[i]) * (B[j] - Cc.CC[j]) + (C[i] - Cc.CC[i]) * (C[j] - Cc.CC[j]));
					if (i == j) { Cc.COVC[i][j]++; }
				}
			}
		}
		cout << endl;
		cout << "Core: " << endl; //выводим ядро класса
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				if (step == 0) { cout << Ac.CA[10 * i + j] << " "; }
				if (step == 1) { cout << Bc.CB[10 * i + j] << " "; }
				if (step == 2) { cout << Cc.CC[10 * i + j] << " "; }
			}
			cout << endl;
		}
		cout << endl;
		if (step == 0) { E_A(Ac.COVA); } // обратная матрица ковариации
		if (step == 1) { E_A(Bc.COVB); }
		if (step == 2) { E_A(Cc.COVC); }
	}
	for (int step = 0; step < 3; step++) {
		cout << "Enter the new member" << endl;
		for (int i = 0; i < 10; i++) {
			cin >> start;
			pic.push_back(start);
			for (int j = 0; j < 10; j++) {
				Ac.RAZA[10 * i + j] = start[j] - 48 - Ac.CA[10 * i + j];  // (x - y)^T
				Bc.RAZB[10 * i + j] = start[j] - 48 - Bc.CB[10 * i + j];
				Cc.RAZC[10 * i + j] = start[j] - 48 - Cc.CC[10 * i + j];
				if (start[j] - 48 == 0) { pic[i][j] = ' '; }
				else (pic[i][j] = char(219));
			}
		}
		cout << endl;
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < 10; j++) {
				cout << pic[i][j]; 
			}
			cout << endl;
		}
		cout << endl;
		for (int i = 0; i < 100; i++) { // (x-y)^T * S^(-1)
			float s1 = 0; float s2 = 0; float s3 = 0; float s4 = 0;
			for (int j = 0; j < 100; j++) {
				s1 = s1 + Ac.RAZA[j];
				s2 = s2 + Bc.RAZB[j];
				s3 = s3 + Cc.RAZC[j];
			}
			Ac.SOVA[i] = s1;
			Bc.SOVB[i] = s2;
			Cc.SOVC[i] = s3;
		}
		for (int i = 0; i < 100; i++) {// (x-y)^T * S^(-1) * (x-y)
			Ac.final1 = Ac.final1 + Ac.SOVA[i] * Ac.RAZA[i];
			Bc.final2 = Bc.final2 + Bc.SOVB[i] * Bc.RAZB[i];
			Cc.final3 = Cc.final3 + Cc.SOVC[i] * Cc.RAZC[i];
		}
		Ac.final1 = sqrt(Ac.final1); // sqrt((x-y)^T * S^(-1) * (x-y))
		Bc.final2 = sqrt(Bc.final2);
		Cc.final3 = sqrt(Cc.final3);
		cout << "Distance to the class A: " << Ac.final1 << endl;
		cout << "Distance to the class B: " << Bc.final2 << endl;
		cout << "Distance to the class C: " << Cc.final3 << endl;
		if ((Ac.final1 >= 3) and (Bc.final2 >= 3) and (Cc.final3 >= 3)) { cout << "Object not in class"; exit; }
		else if ((Ac.final1 <= Bc.final2) and (Ac.final1 <= Cc.final3)) { cout << "Object belongs to the class A"; }
		else if ((Bc.final2 <= Ac.final1) and (Bc.final2 <= Cc.final3)) { cout << "Object belongs to the class B"; }
		else if ((Cc.final3 <= Ac.final1) and (Cc.final3 <= Bc.final2)) { cout << "Object belongs to the class C"; };
		cout << endl << endl;
	}
}