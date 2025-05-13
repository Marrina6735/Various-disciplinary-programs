#include "Database.cpp"
#include <random>

int main() {
    int n = 10;
    Database db1;
    Database db2;
    for (int i=0;i<n;i++){
        db1.add(new Element(i));
        db2.add(new Element(i));
    }

    auto rng = std::default_random_engine {};
    std::shuffle(std::begin(db1.arr), std::end(db1.arr), rng);
    std::shuffle(std::begin(db2.arr), std::end(db2.arr), rng);
    db1.del(3);
    db2.del(3);
    db1.add(new Element(3));
    db2.add(new Element(3));
    cout << "set1 not sort " << db1.op << endl;
    cout << "set2 not sort " << db2.op << endl << endl;

    db1.op_b = 0;
    db1.op_qs = 0;
    db2.op_b = 0;
    db2.op_qs = 0;
    db1.bubbleSort();
    db2.bubbleSort();
    std::shuffle(std::begin(db1.arr), std::end(db1.arr), rng);
    std::shuffle(std::begin(db2.arr), std::end(db2.arr), rng);
    db1.quickSort(0, db1.arr.size()-1);
    db2.quickSort(0, db2.arr.size()-1);
    db1.del(3);
    db2.del(3);
    db1.add(new Element(3));
    db2.add(new Element(3));

    cout << "set1 bubbleSort " << db1.op_b << endl;
    cout << "set1 quickSort " << db1.op_qs << endl << endl;
    cout << "set2 bubbleSort " << db2.op_b << endl;
    cout << "set2 quickSort " << db2.op_qs << endl;
    db1.print();
    db2.print();
    return 0;
}
