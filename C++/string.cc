#include <iostream>
#include <string>
using namespace std;
int main()
{
    string firstName = "Liz";
    string lastName = "Boese";
    cout << firstName << lastName << endl;

    int length = firstName.length( );
    cout << length;

    string fullName = firstName + lastName;
    cout << fullName << endl;
    string partial = fullName.substr(2,5);
    cout << partial;
    return 0;
}
// what does this print?! // what does this print?! // what does this print?! // what does this print?!
