// Ma and Pa Point of Sale System
// Created by the CS150 Class
#include <iostream>
using namespace std;

const double NICKEL = 1.0/20.0;
const double DIME = 1.0/10.0;

int main()
{
    double totalsales = 0.0;
    double predictedsales = 0.0;
    const int dimeitems = 10000;
    const int nickelitems = 10000;


    predictedsales = (dimeitems*10 + nickelitems*5)/100;

    for (int i = 0; i < dimeitems; i++)
    {
        totalsales += DIME;
    }
    for (int i = 0; i < nickelitems; i++)
    {
        totalsales += NICKEL;
    }

    cout << "Predicted Sales = $" << predictedsales << endl;
    cout << "Total Sales = $" << totalsales << endl;

    if (predictedsales == totalsales)
    {
        cout << "Register Balanced" << endl;
    }
    else
    {
        cout << "Register Not Balanced" << endl;
    }

    return 0;
}