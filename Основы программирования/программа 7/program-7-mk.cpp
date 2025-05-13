#include <iostream>
#include <fstream>
#include <string>

using namespace std;

void replacement(string* line, string a, string b) { // Замена последовательности символов
	while ((int)line -> find(a) != -1) {
		line -> replace(line -> find(a), a.length(), b);
	}
}

int main() {
	string line;
	string line_ch;
	string line_replace;
	ifstream f("input.txt"); // Работа с файлом в режиме чтения (считывания)
	if (f.is_open()) {
		getline(f, line);
		getline(f, line_ch);
		getline(f, line_replace);
		ofstream out("output.txt"); // Работа с файлом в режиме записи
		replacement(&line, line_ch, line_replace);
		out << line;
		out.close();
		f.close(); // Закрытие файла
		cout << "Строка с замененными символами находится в файле output.txt ";
	}
	else cout << "Запишите Вашу строку и две последовательности символов в файл input.txt ";
}