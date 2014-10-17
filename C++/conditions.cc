//conditions
#include <iostream>
using namespace std;

int main()
{
    char option = 'Z';
    int aCount = 0;
    int bCount = 0;
    int cCount = 0;
    switch (option)
    {
        case 'A':
            aCount++;
            break;
        case 'B':
            bCount++;
            break;
        case 'C':
            cCount++;
            break;
        default:
            cout << "does not match" << endl;
    }
    cout << option <<endl;
    cout << "A's:" << aCount << "B's:" << bCount << "C's:" << cCount <<endl;
}
