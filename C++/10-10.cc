#include<iostream>
using namespace std;
int main(){
    double num = 123.456789;
    cout.precision(3);
    cout << fixed << num << endl;

    double num2 = 98765.4321;
    cout << num2 << endl;
    cout << num++ << endl;
    cout << ++num << endl;
    return 0;
}
