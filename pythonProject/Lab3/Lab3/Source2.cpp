#include "Source1.cpp"
#include <random>
#include <time.h>

int main() {
    int n = 1500;
    Database db1;
    Database db2;
    for (int i = 0; i < n; i++) {
        db1.add(new Element(i));
        db2.add(new Element(i));
    }
    auto rng = default_random_engine(time(0));

    char act;
    do {
        cout << "Set1: " << db1.op << endl;
        cout << "Set2: " << db2.op << endl << endl;
        cout << "Choose an action: " << endl;
        cout << "1) shuffle " << endl;
        cout << "2) delete and add an element " << endl;
        cout << "3) clear " << endl;
        cout << "4) sort (set1 - quickSort, set2 - bubbleSort) " << endl;
        cout << "0) exit " << endl;
        cin >> act;
        switch (act) {
        case '1':
            shuffle(begin(db1.arr), end(db1.arr), rng);
            shuffle(begin(db2.arr), end(db2.arr), rng);
            cout << "shuffled" << endl << endl;
            break;
        case '2':
            db1.del(2);
            db2.del(2);
            db1.add(new Element(2));
            db2.add(new Element(2));
            cout << "deleted and added an element 2" << endl << endl;
            break;
        case '3':
            db1.op = 0;
            db1.op_b = 0;
            db1.op_qs = 0;
            db2.op = 0;
            db2.op_b = 0;
            db2.op_qs = 0;
            cout << "Options cleared" << endl << endl;
            break;
        case '4':
            db1.quickSort(0, db1.arr.size() - 1);
            db2.bubbleSort();
            cout << "Sets sorted (quickSort: " << db1.op_qs << ", bublleSort: " << db2.op_b << ")" << endl << endl;
            break;
        }
    } while (act != '0');

    return 0;
}
