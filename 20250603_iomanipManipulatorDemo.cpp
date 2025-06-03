#include <iostream>
#include <iomanip>
using namespace std;

int main() {
    double pi = 3.141592653589;
    int num = 42;

    cout << "==== Fixed vs Scientific ====" << endl;
    cout << "Default:       " << pi << endl;
    cout << "Fixed:         " << fixed << setprecision(4) << pi << endl;
    cout << "Scientific:    " << scientific << setprecision(4) << pi << endl;

    cout << "\n==== setprecision (without fixed) ====" << endl;
    cout << "Precision(2):  " << setprecision(2) << 123.456 << endl;  // significant digits
    cout << "Precision(6):  " << setprecision(6) << 123.456 << endl;

    cout << "\n==== setw and setfill ====" << endl;
    cout << "Default:       [" << num << "]" << endl;
    cout << "setw(5):       [" << setw(5) << num << "]" << endl;
    cout << "setw + fill:   [" << setfill('0') << setw(5) << num << "]" << endl;

    cout << "\n==== Alignment ====" << endl;
    cout << left;
    cout << "Left aligned:  [" << setw(10) << num << "]" << endl;
    cout << right;
    cout << "Right aligned: [" << setw(10) << num << "]" << endl;
    cout << internal;
    cout << "Internal align:[" << setw(10) << -num << "]" << endl;

    cout << "\n==== Boolean Output ====" << endl;
    cout << "Default bool:  " << (true) << " " << (false) << endl;
    cout << boolalpha;
    cout << "With boolalpha:" << true << " " << false << endl;
    cout << noboolalpha;
    cout << "Back to int:   " << true << " " << false << endl;

    cout << "\n==== Integer Bases ====" << endl;
    cout << "Decimal:       " << dec << 255 << endl;
    cout << "Hexadecimal:   " << hex << 255 << endl;
    cout << "Octal:         " << oct << 255 << endl;

    return 0;
}
