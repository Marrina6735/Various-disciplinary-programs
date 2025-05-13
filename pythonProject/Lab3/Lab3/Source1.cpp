#include <vector>
#include <iostream>
#include <algorithm>
#include "Element.cpp"
using namespace std;

struct Database { // Cортировка по возрастанию
    vector<Element*> arr;
    bool sorted = false;
    int op_qs = 0;
    int op_b = 0;
    int op = 0;
    void add(Element* count) {
        if (sorted) {
            for (int i = 0; i < arr.size(); i++) {
                op++;
                if (arr.at(i)->id > count->id) {
                    arr.insert(arr.begin() + i, count);
                    break;
                }
            }
        }
        else {
            arr.emplace_back(count);
        }
    }

    int search(int idd) {
        if (sorted) {
            int down = 0;
            int up = arr.size() - 1;
            while (down != up) {
                op++;
                int middle = (down + up) / 2;
                if (idd == arr.at(middle)->id) {
                    return middle;
                }
                else if (idd > arr.at(middle)->id) {
                    down = middle + 1;
                }
                else up = middle - 1;
            }
        }
        else {
            for (int i = 0; i < arr.size(); i++) {
                op++;
                if (arr.at(i)->id == idd) {
                    return i;
                }
            }
        }
    }

    void del(int idd) {
        int index = search(idd);
        delete arr.at(index);
        arr.erase(arr.begin() + index);
    }

    void print() {
        for (int i = 0; i < arr.size(); i++) {
            cout << i + 1 << ". " << arr.at(i)->id << endl;
        }
        cout << endl;
    }

    void bubbleSort() { // Сортировка пузырьком
        for (int i = 0; i < arr.size(); i++) {
            for (int j = i; j < arr.size(); j++) {
                op_b++;
                if (arr.at(i)->id > arr.at(j)->id) {
                    swap(arr.at(i), arr.at(j));
                }
            }
        }
        sorted = true;
    }

    int section(int l, int h) {
        int x = arr.at(h)->id;
        int i = (l - 1);
        for (int j = l; j <= h - 1; j++) {
            if (arr.at(j)->id <= x) {
                i++;
                swap(arr.at(i), arr.at(j));
            }
        }
        swap(arr.at(i + 1), arr.at(h));
        return (i + 1);
    }

    void quickSort(int low, int high) { // Быстрая сортировка
        if (low < high) {
            int pos = section(low, high);
            quickSort(low, pos - 1);
            quickSort(pos + 1, high);
        }
    }
};
