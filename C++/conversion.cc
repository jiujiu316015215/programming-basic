#include <iostream>
#include <string>
#include <iomanip>
using namespace std;
int main(int argc, char*argv[])
{
    cout <<"hi!" <<endl;

    string string2 = "42.23";
    double value2 = stod(string2);
    cout << value2 * 2 << endl;

    //prompting for user input
    cout << "What yo name?" << endl;
    string name;
    cin >> name;
    cout << "Weacome," << name << endl;

    // play with CLA
    cout << argc << endl;
    cout << argv[1] << endl;

    // Formatting numbers
    cout << fixed << setprecision(2);
}
